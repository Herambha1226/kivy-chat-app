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
from kivymd.uix.list import MDList,OneLineAvatarIconListItem,IconLeftWidget,OneLineListItem
from kivymd.toast import toast
from kivy.clock import Clock
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
        friend_id = self.get_friend_id(friend_name)

        if friend_id is None:
            print("Friend ID not found")
            return

        chatting_screen = self.manager.get_screen("chatting")
        chatting_screen.friend_name = friend_name
        chatting_screen.friend_id = friend_id

        self.manager.current = "chatting"


    def move_to_all_users(self, *args):
        self.manager.current = "all_users"

    def refresh_friend_list(self):
        self.list.clear_widgets()  # ⭐ VERY IMPORTANT

        for friend in self.friends:
            item = OneLineAvatarIconListItem(
                text=friend["user_name"],
                on_release=self.move_to_chat
            )
            icon = IconLeftWidget(icon="account")
            item.add_widget(icon)
            self.list.add_widget(item)

    def load_friends(self):
        user_id = getattr(self.manager, "user_id", None)
        url = f"http://127.0.0.1:5000/get_friends/{user_id}"

        try:
            response = requests.get(url)
            data = response.json()

            self.friends.clear()  # clear old data

            if "friends" in data:
                for friend in data["friends"]:
                    self.friends.append(friend)

                self.refresh_friend_list()  # ⭐ UPDATE UI PROPERLY

        except Exception as e:
            print("Error fetching friends:", e)
            toast("Fetching Error")
    def get_friend_id(self, friend_name):
        for friend in self.friends:
            if friend["user_name"] == friend_name:
                return friend["id"]
        return None


from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout

class MessageBubble(AnchorLayout):
    def __init__(self, text, sender="me", **kwargs):
        super().__init__(**kwargs)

        self.size_hint_y = None
        self.anchor_x = "right" if sender == "me" else "left"
        self.padding = (dp(10), dp(5))

        # Bubble Card
        bubble = MDCard(
            padding=dp(10),
            md_bg_color=(0.2, 0.6, 1, 1) if sender == "me" else (0.3, 0.3, 0.3, 1),
            radius=[15, 15, 15, 15],
            size_hint=(None, None),
        )

        # Label
        label = MDLabel(
            text=text,
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            size_hint=(None, None),
            text_size=(dp(250), None),  # max width
        )

        # Let label calculate height automatically
        label.bind(
            texture_size=lambda instance, value: setattr(instance, "size", value)
        )

        bubble.add_widget(label)

        # Adjust bubble size after label updates
        def update_bubble_size(*args):
            bubble.size = (label.width + dp(20), label.height + dp(20))
            self.height = bubble.height + dp(10)

        label.bind(size=update_bubble_size)

        self.add_widget(bubble)





class chatting(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.friend_name = ""
        name="chatting"

        # MAIN VERTICAL LAYOUT (VERY IMPORTANT)
        main_layout = MDBoxLayout(
            orientation="vertical",
            size_hint=(1, 1),
            md_bg_color=get_color_from_hex("#3B516E"),
        )

        # 🔹 HEADER (Friend Card - Top)
        friend_info = MDCard(
            size_hint=(1, 0.12),
            md_bg_color=get_color_from_hex("#A4A5A6"),
            padding=10
        )

        header_layout = MDBoxLayout(
            orientation="horizontal"
        )

        back_btn = MDIconButton(
            icon="arrow-left",
            on_release=self.back_to_chat_list
        )

        self.header = MDLabel(
            text="",
            halign="center",
            font_style="H5"
        )

        header_layout.add_widget(back_btn)
        header_layout.add_widget(self.header)
        friend_info.add_widget(header_layout)

        # 🔹 CHAT SCROLL (Middle - UNDER HEADER)
        self.scroll = MDScrollView(
            size_hint=(1, 0.78)
        )

        self.chat_list = MDList()
        self.chat_list.size_hint_y = None
        self.chat_list.bind(minimum_height=self.chat_list.setter("height"))
        self.scroll.add_widget(self.chat_list)

        # 🔹 TEXT INPUT CARD (Bottom)
        text_card = MDCard(
            size_hint=(1, 0.1),
            md_bg_color=get_color_from_hex("#A4A5A6"),
            padding=10
        )

        input_layout = MDBoxLayout(
            orientation="horizontal",
            spacing=10
        )

        self.text_field = MDTextField(
            mode="round",
            hint_text="message...",
            size_hint_x=0.85,
            text_color_focus= get_color_from_hex("#3B516E"),
            line_color_focus = get_color_from_hex("#3B516E")
        )

        send_btn = MDIconButton(
            icon="send",
            on_release=lambda x: self.send_message(self.text_field.text)
        )

        input_layout.add_widget(self.text_field)
        input_layout.add_widget(send_btn)
        text_card.add_widget(input_layout)

        # ADD ALL IN ORDER (TOP → MIDDLE → BOTTOM)
        main_layout.add_widget(friend_info)
        main_layout.add_widget(self.scroll)
        main_layout.add_widget(text_card)

        self.add_widget(main_layout)


    def back_to_chat_list(self,*args):
        self.manager.current = "home"
    
    def on_pre_enter(self, *args):
        self.header.text = self.friend_name
        self.load_messages()
        self.event = Clock.schedule_interval(self.auto_refresh,2)

    def auto_refresh(self,dt):
        self.load_messages()

    def on_leave(self, *args):
        if hasattr(self,'event'):
            self.event.cancel()
    
    def send_message(self, message_text):
        url = "http://127.0.0.1:5000/send_message"

        data = {
            "sender_id": self.manager.user_id,
            "receiver_id": self.friend_id,  # store when opening chat
            "message": message_text
        }

        try:
            response = requests.post(url, json=data)
            result = response.json()
            print(result)

            # Reload chat after sending
            self.load_messages()
            self.text_field.text = ""

        except Exception as e:
            print("Send error:", e)
    
    def load_messages(self):
        url = "http://127.0.0.1:5000/get_messages"

        data = {
            "user_id": self.manager.user_id,
            "friend_id": self.friend_id
        }

        try:
            response = requests.post(url, json=data)
            messages = response.json().get("messages", [])

            # Clear old UI messages
            self.chat_list.clear_widgets()

            for msg in messages:
                text = msg["message"]
                sender = msg["sender_id"]

                if sender == self.manager.user_id:
                    bubble = MessageBubble(text=text, sender="me")
                else:
                    bubble = MessageBubble(text=text, sender="friend")

                self.chat_list.add_widget(bubble)

            if self.scroll.scroll_y < 0.05:
                # Auto scroll to bottom
                self.scroll.scroll_y = 0

        except Exception as e:
            print("Auto refresh error:", e)





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
            url = "http://127.0.0.1:5000/add_friend"
            data = {
                "user_id":self.manager.user_id,
                "friend_name":friend_name
            }
            try:
                response = requests.post(url,json=data)
                result = response.json()
                toast(result["message"])
                self.manager.current = "home"
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