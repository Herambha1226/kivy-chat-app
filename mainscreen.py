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
            text_color=get_color_from_hex("#A4A5A6")
        )

        # Scroll View Adding 
        scroll = MDScrollView()

        self.list = MDList()

        friends = ["self(You)"]

        for name in friends:
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
    
    def move_to_chat(self,*args):
        self.manager.current = "chatting"

class chatting(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        name = "chatting"

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

        friend_info.add_widget(back_btn)

        main_card.add_widget(friend_info)

        text_card.add_widget(text_field)
        text_card.add_widget(send_btn)

        layout.add_widget(main_card)
        layout.add_widget(text_card)

        self.add_widget(layout)

    def back_to_chat_list(self,*args):
        self.manager.current = "home"




class Example(MDApp):
    def build(self):
        sm = MDScreenManager()
        sm.add_widget(home(name="home"))
        sm.add_widget(chatting(name="chatting"))
        return sm

if __name__ == "__main__":
    Example().run()