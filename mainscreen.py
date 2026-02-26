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
class home(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        name = "home"

        layout = MDFloatLayout()

        main_card = MDCard(
            size_hint = (1,1),
            md_bg_color=get_color_from_hex("#3B516E"), 
        )

        main_label = MDLabel(
            text="Herambha",
            theme_text_color= "Custom",
            text_color=get_color_from_hex("#A4A5A6"),
            halign="center",
            pos_hint={"center_y":0.95,"center_x":0.5},
            font_style="H4",
            bold=True,
            font_family="Roboto",
        )

        norm_card = MDCard(
            size_hint = (1,0.85),
            md_bg_color = get_color_from_hex("#A4A5A6"),
            radius = [20,20,0,0],
            padding=20,
            elevation=5
        )

        add_friend = MDCard(
            size_hint = (0.09,0.09),
            md_bg_color = get_color_from_hex("#3B516E"),
            pos_hint = {"center_x" : 0.9,"center_y":0.1},
        )
        plus_icon = MDIconButton(
            icon="plus",
            pos_hint = {"center_x":0.5,"center_y":0.5,'x':0.5},
            theme_text_color="Custom",
            text_color=get_color_from_hex("#A4A5A6"),
            on_release=self.move_to_all_users
        )

        # Scroll View Adding 
        scroll = MDScrollView()

        self.list = MDList()

        self.friends = ["self(You)"]

        for name in self.friends:
            item = OneLineAvatarIconListItem(
                text=name,
                on_release=self.move_to_chat
            )
            icon = IconLeftWidget(icon="account")
            item.add_widget(icon)
            self.list.add_widget(item)
        
        scroll.add_widget(self.list)
        
        norm_card.add_widget(scroll)



        main_card.add_widget(main_label)
        
        add_friend.add_widget(plus_icon)

        layout.add_widget(main_card)
        layout.add_widget(norm_card)
        layout.add_widget(add_friend)

        self.add_widget(layout)
    
    def move_to_chat(self,instance):
        friend_name = instance.text
        self.manager.get_screen("chatting").friend_name = friend_name
        self.manager.current = "chatting"
    def move_to_all_users(self,*args):
        self.manager.current = "all_users"
    def refresh_friend_list(self):
        self.list.clear_widgets()

        for name in self.friends:
            item = OneLineAvatarIconListItem(
                text=name,
                on_release=self.move_to_chat
            )
            icon = IconLeftWidget(icon="account")
            item.add_widget(icon)
            self.list.add_widget(item)


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

        name = "all_users"

        layout = MDFloatLayout()

        main_card = MDCard(
            size_hint = (1,1),
            md_bg_color = get_color_from_hex("#3B516E")
        )

        header_text = MDLabel(
            text = "New Friends",
            pos_hint = {'center_x':0.5,"center_y":0.95},
            halign="center",
            font_style="H4",
            bold=True,
            theme_text_color="Custom",
            text_color=get_color_from_hex("#A4A5A6") 
        )

        back_btn = MDIconButton(
            icon = "arrow-left",
            pos_hint={"center_x":0.08,"center_y":0.95},
            theme_text_color="Custom",
            text_color=get_color_from_hex("#A4A5A6"),
            on_release=self.move_to_back
        )

        nxt_layer_card = MDCard(
            size_hint = (1,0.88),
            md_bg_color = get_color_from_hex("#A4A5A6") 
        )

        scroll = MDScrollView()

        self.list = MDList()

        temp_friends = ["Herambha","Karthikeya","Guptha","Gayathri","Eswara Rao","Namratha"]

        self.friends = ["self(You)"]

        for name in temp_friends:
            if name not in self.friends:
                item = OneLineAvatarIconListItem(
                    text=name,
                )
                icon = IconLeftWidget(icon="account")
                item.add_widget(icon)

                add_btn = IconRightWidget(
                    icon = "account-plus",
                    on_release=lambda x, n=name: self.add_friend(n)
                )
                item.add_widget(add_btn)
                self.list.add_widget(item)
        
        scroll.add_widget(self.list)
        nxt_layer_card.add_widget(scroll)


        main_card.add_widget(back_btn)
        main_card.add_widget(header_text)
        

        layout.add_widget(main_card)
        layout.add_widget(nxt_layer_card)

        self.add_widget(layout)
    def move_to_back(self,*args):
        self.manager.current = "home"
    
    def add_friend(self,friend_name):
        if friend_name not in self.friends:
            self.friends.append(friend_name)
            friend_screen = self.manager.get_screen("home")
            friend_screen.friends.append(friend_name)
            friend_screen.refresh_friend_list()
            self.manager.current = "home"
            toast("Friend Added Successfully 👍")
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