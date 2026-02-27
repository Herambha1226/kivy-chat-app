from kivymd.uix.pickers.datepicker.datepicker import date
from kivymd.uix.list import IconRightWidget
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDIconButton,MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import MDList,OneLineAvatarIconListItem,IconLeftWidget
from kivymd.toast import toast
import requests


class home(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        name = "home"

        self.friends = []  # ⭐ IMPORTANT

        layout = MDFloatLayout()

        main_card = MDCard(
            size_hint=(1, 1),
            md_bg_color=get_color_from_hex("#3B516E"),
        )

        main_label = MDLabel(
            text="Herambha",
            theme_text_color="Custom",
            text_color=get_color_from_hex("#A4A5A6"),
            halign="center",
            pos_hint={"center_y": 0.95, "center_x": 0.5},
            font_style="H4",
            bold=True,
        )

        norm_card = MDCard(
            size_hint=(1, 0.85),
            pos_hint={"y": 0},
            md_bg_color=get_color_from_hex("#A4A5A6"),
            radius=[20, 20, 0, 0],
            padding=20,
            elevation=5
        )

        add_friend = MDCard(
            size_hint=(0.09, 0.09),
            md_bg_color=get_color_from_hex("#3B516E"),
            pos_hint={"center_x": 0.9, "center_y": 0.1},
        )

        plus_icon = MDIconButton(
            icon="plus",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            theme_text_color="Custom",
            text_color=get_color_from_hex("#A4A5A6"),
            on_release=self.move_to_all_users
        )

        # ✅ CORRECT SCROLL SETUP (ONLY ONE CHILD)
        scroll = MDScrollView()
        self.list = MDList()
        scroll.add_widget(self.list)
        norm_card.add_widget(scroll)

        main_card.add_widget(main_label)
        add_friend.add_widget(plus_icon)

        layout.add_widget(main_card)
        layout.add_widget(norm_card)
        layout.add_widget(add_friend)

        self.add_widget(layout)

    def on_enter(self):
        self.load_friends()  # auto load when screen opens

    def move_to_chat(self, instance):
        friend_name = instance.text
        self.manager.get_screen("chatting").friend_name = friend_name
        self.manager.current = "chatting"

    def move_to_all_users(self, *args):
        self.manager.current = "all_users"

    def refresh_friend_list(self):
        self.list.clear_widgets()  # ⭐ VERY IMPORTANT

        for name in self.friends:
            item = OneLineAvatarIconListItem(
                text=name,
                on_release=self.move_to_chat
            )
            icon = IconLeftWidget(icon="account")
            item.add_widget(icon)
            self.list.add_widget(item)

    def load_friends(self):
        user_id = self.manager.user_id
        url = f"http://127.0.0.1:5000/get_friends/{user_id}"

        try:
            response = requests.get(url)
            data = response.json()
            print(data)

            self.friends.clear()  # clear old data

            if "friends" in data:
                for friend in data["friends"]:
                    self.friends.append(friend["user_name"])

                self.refresh_friend_list()  # ⭐ UPDATE UI PROPERLY

        except Exception as e:
            print("Error fetching friends:", e)
            toast("Fetching Error")




class chatting(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        name = "chatting"

        self.friend_name = ""

        layout = MDFloatLayout()


        main_card = MDCard(
            size_hint = (1,1),
            md_bg_color = get_color_from_hex("#3B516E")
        )

        text_card = MDCard(
            size_hint = (1,0.1),
            md_bg_color=get_color_from_hex("#A4A5A6")
        )

        text_field = MDTextField(
            mode = "round",
            size_hint_x =0.8,
            pos_hint = {"center_x":0.5,"center_y":0.5},
            text_color_focus= get_color_from_hex("#3B516E"),
            hint_text="message..."
        )
        send_btn = MDIconButton(
            icon="send",
            pos_hint = {"center_y":0.5}
        )

        friend_info = MDCard(
            size_hint = (1,0.2),
            pos_hint = {"center_x":0.5,"center_y":1},
            md_bg_color = get_color_from_hex("#A4A5A6")
        )

        back_btn = MDIconButton(
            icon= "arrow-left",
            pos_hint = {"center_x":0.1,"center_y":0.3},
            on_release=self.back_to_chat_list
        )

        self.header = MDLabel(
            text = "",
            halign="center",
            font_style="H5",
            pos_hint={"center_x":0.5,"center_y":0.3}
        )

        friend_info.add_widget(back_btn)
        friend_info.add_widget(self.header)

        main_card.add_widget(friend_info)

        text_card.add_widget(text_field)
        text_card.add_widget(send_btn)

        layout.add_widget(main_card)
        layout.add_widget(text_card)

        self.add_widget(layout)

    def back_to_chat_list(self,*args):
        self.manager.current = "home"
    
    def on_pre_enter(self, *args):
        self.header.text = self.friend_name




class all_users(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = MDFloatLayout()

        main_card = MDCard(
            size_hint=(1, 1),
            md_bg_color=get_color_from_hex("#3B516E")
        )

        header_text = MDLabel(
            text="New Friends",
            pos_hint={'center_x': 0.5, "center_y": 0.95},
            halign="center",
            font_style="H4",
            bold=True,
            theme_text_color="Custom",
            text_color=get_color_from_hex("#A4A5A6")
        )

        back_btn = MDIconButton(
            icon="arrow-left",
            pos_hint={"center_x": 0.08, "center_y": 0.95},
            theme_text_color="Custom",
            text_color=get_color_from_hex("#A4A5A6"),
            on_release=self.move_to_back
        )

        nxt_layer_card = MDCard(
            size_hint=(1, 0.88),
            md_bg_color=get_color_from_hex("#A4A5A6")
        )

        # 🔥 Scroll + List (IMPORTANT)
        self.scroll = MDScrollView()
        self.list = MDList()
        self.scroll.add_widget(self.list)
        nxt_layer_card.add_widget(self.scroll)

        main_card.add_widget(back_btn)
        main_card.add_widget(header_text)

        layout.add_widget(main_card)
        layout.add_widget(nxt_layer_card)

        self.add_widget(layout)

        # Data containers
        self.all_friends = []
        self.friends = ["self(You)"]

    def move_to_back(self, *args):
        self.manager.current = "home"

    def on_enter(self):
        # 🔥 Auto load users when screen opens
        self.get_all_users()

    # 🚀 MAIN WORKING FUNCTION
    def get_all_users(self):
        url = "http://127.0.0.1:5000/all_friends"

        try:
            response = requests.get(url)
            data = response.json()

            print("API DATA:", data)

            # 🔥 CLEAR OLD UI (VERY IMPORTANT)
            self.list.clear_widgets()
            self.all_friends.clear()

            if "friends" in data:
                for friend in data["friends"]:
                    name = friend["user_name"]

                    # Skip if already in friend list
                    if name not in self.friends:
                        self.all_friends.append(name)

                        # 🔥 CREATE UI ITEM DYNAMICALLY
                        item = OneLineAvatarIconListItem(text=name)

                        icon = IconLeftWidget(icon="account")
                        item.add_widget(icon)

                        add_btn = IconRightWidget(
                            icon="account-plus",
                            on_release=lambda x, n=name: self.add_friend(n)
                        )
                        item.add_widget(add_btn)

                        self.list.add_widget(item)

        except Exception as e:
            toast("Error Getting Users")
            print("Error:", e)

    
    def add_friend(self,friend_name):
        if friend_name not in self.friends:
            """self.friends.append(friend_name)
            friend_screen = self.manager.get_screen("home")
            friend_screen.friends.append(friend_name)
            friend_screen.refresh_friend_list()
            self.manager.current = "home"""

            url = "http://127.0.0.1:5000/add_friend"
            data = {
                "friend_name":friend_name
            }
            try:
                response = requests.post(url,json=data)
                result = response.json()
                toast(result["message"])
            except Exception as e:
                toast("Adding Friend is Not work")
        else:
            toast("Friend Already Exists 💀")
        



"""class Example(MDApp):
    def build(self):
        sm = MDScreenManager()
        sm.add_widget(home(name="home"))
        sm.add_widget(chatting(name="chatting"))
        sm.add_widget(all_users(name="all_users"))
        return sm"""
"""
if __name__ == "__main__":
    Example().run()"""