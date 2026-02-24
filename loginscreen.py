from kivymd.uix.backdrop.backdrop import MDFloatLayout
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton,MDRaisedButton,MDTextButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.textfield import MDTextField
from kivy.utils import get_color_from_hex

class Start_Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = "start"

        layout = MDFloatLayout()

        card1 = MDCard(
            size_hint=(1,1),
            md_bg_color=get_color_from_hex("#3B516E"),
        )

        label1= MDLabel(
            text = "Herambha",
            font_style = "H4",
            theme_text_color = "Custom",
            halign = "center",
            text_color=get_color_from_hex("#A4A5A6"),
            bold = True,
            font_family="Roboto",
            pos_hint={"center_x":0.5,"center_y":0.85}
        )

        card2 = MDCard(
            size_hint=(1,0.7),
            padding=20,
            radius=[20,20,0,0],
            pos_hint={"x":0,"y":0},
            md_bg_color = get_color_from_hex("#A4A5A6"),
            elevation=5
        )

        label2 = MDLabel(
            text="Here herambha created app this will helps communication !",
            text_color=get_color_from_hex("#0C0E0F"),
            theme_text_color="Custom",
            halign="center",
            font_style="H6",
            bold=True,
            pos_hint={"center_x":0.5,"center_y":0.3}
            
        )

        button = MDRaisedButton(
            text="Get Start",
            pos_hint={"center_x":0.5,"center_y":0.1},
            md_bg_color=get_color_from_hex("#3B516E"),
            theme_text_color = "Custom",
            text_color = get_color_from_hex("#A4A5A6"),
            size_hint=(1,0.1),
            on_release=self.go_to_login
        )

        inner_layout = MDFloatLayout()
        inner_layout.add_widget(label2)
        inner_layout.add_widget(button)
        
        card2.add_widget(inner_layout)

        layout.add_widget(card1)
        layout.add_widget(card2)
        layout.add_widget(label1)

        #card1.add_widget(card2)
        #layout.add_widget(card1)

        self.add_widget(layout)

    def go_to_login(self, *args):
        self.manager.current = "login"

class Login_Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = "login"

        layout = MDFloatLayout()

        card1 = MDCard(
            size_hint=(1,1),
            md_bg_color=get_color_from_hex("#3B516E"),
        )
        back_button =MDIconButton(
            icon = "arrow-left",
            pos_hint={"center_x":0.08,"center_y":0.92},
            theme_text_color="Custom",
            text_color=get_color_from_hex("#A4A5A6"),
            on_release=self.go_to_back
        )

        label1= MDLabel(
            text = "Herambha",
            font_style = "H4",
            theme_text_color = "Custom",
            halign = "center",
            text_color=get_color_from_hex("#A4A5A6"),
            bold = True,
            font_family="Roboto",
            pos_hint={"center_x":0.5,"center_y":0.85}
        )

        card2 = MDCard(
            size_hint=(1,0.7),
            padding=20,
            radius=[20,20,0,0],
            pos_hint={"x":0,"y":0},
            md_bg_color = get_color_from_hex("#A4A5A6"),
            elevation=5
        )
        log_label = MDLabel(
            text = "Login",
            text_color=get_color_from_hex("#0C0E0F"),
            theme_text_color="Custom",
            halign="center",
            font_style="H5",
            bold=True,
            pos_hint={"center_x":0.5,"center_y":1}
        )

        user_name = MDLabel(
            text="User Name",
            text_color=get_color_from_hex("#0C0E0F"),
            theme_text_color="Custom",
            halign="left",
            font_style="H5",
            bold=True,
            pos_hint={"X":0.07,"center_y":0.85}
        )

        user_input = MDTextField(
            mode="rectangle",
            icon_left="account",
            text_color_focus= get_color_from_hex("#3B516E"),
            icon_left_color_focus = get_color_from_hex("#3B516E"),
            line_color_focus = get_color_from_hex("#3B516E"),
            pos_hint={"center_x":0.5,"center_y":0.7}
        )
        user_password = MDLabel(
            text="Password",
            text_color=get_color_from_hex("#0C0E0F"),
            theme_text_color="Custom",
            halign="left",
            font_style="H5",
            bold=True,
            pos_hint={"X":0.07,"center_y":0.55}
        )
        pass_input = MDTextField(
            mode="rectangle",
            icon_left="eye",
            text_color_focus= get_color_from_hex("#3B516E"),
            icon_left_color_focus = get_color_from_hex("#3B516E"),
            line_color_focus = get_color_from_hex("#3B516E"),
            pos_hint={"center_x":0.5,"center_y":0.42}
        )

        label2 = MDLabel(
            text="Get Back To The Conversation !",
            text_color=get_color_from_hex("#0C0E0F"),
            theme_text_color="Custom",
            halign="center",
            font_style="H6",
            bold=True,
            pos_hint={"center_x":0.5,"center_y":0.3}
            
        )

        button = MDRaisedButton(
            text="Login !",
            pos_hint={"center_x":0.5,"center_y":0.17},
            md_bg_color=get_color_from_hex("#3B516E"),
            theme_text_color = "Custom",
            text_color = get_color_from_hex("#A4A5A6"),
            size_hint=(1,0.1)
        )

        signup_layout = MDBoxLayout(
            orientation="horizontal",
            size_hint=(1,None),
            height="40dp",
            pos_hint={"center_y":0.05},
            padding=("20dp",0)
        )

        signup_label = MDLabel(
            text="Don't have an account? ",
            halign="right",
            font_style="H6",
            theme_text_color="Custom",
            text_color=get_color_from_hex("#0C0E0F")
        )

        signup_button = MDTextButton(
            text="Sign Up",
            theme_text_color="Custom",
            text_color=get_color_from_hex("#0C0E0F"),
            pos_hint={"center_x":0.08},
            on_release=self.go_to_signup
        )

        signup_layout.add_widget(signup_label)
        signup_layout.add_widget(signup_button)

        inner_layout = MDFloatLayout()
        inner_layout.add_widget(log_label)
        inner_layout.add_widget(user_name)
        inner_layout.add_widget(user_input)
        inner_layout.add_widget(user_password)
        inner_layout.add_widget(pass_input)
        inner_layout.add_widget(label2)
        inner_layout.add_widget(button)
        inner_layout.add_widget(signup_layout)  # SignUp buttton for the conection of signup screen
        
        card2.add_widget(inner_layout)

        layout.add_widget(card1)
        layout.add_widget(card2)
        layout.add_widget(label1)
        layout.add_widget(back_button)

        #card1.add_widget(card2)
        #layout.add_widget(card1)

        self.add_widget(layout)
    def go_to_signup(self,*args):
        self.manager.current = "signup"
    def go_to_back(self,*args):
        self.manager.current = "start"

class signup_Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = "signup"

        layout = MDFloatLayout()

        card1 = MDCard(
            size_hint=(1,1),
            md_bg_color=get_color_from_hex("#3B516E"),
        )
        back_button =MDIconButton(
            icon = "arrow-left",
            pos_hint={"center_x":0.08,"center_y":0.92},
            theme_text_color="Custom",
            text_color=get_color_from_hex("#A4A5A6"),
            on_release=self.go_to_back
        )

        label1= MDLabel(
            text = "Herambha",
            font_style = "H4",
            theme_text_color = "Custom",
            halign = "center",
            text_color=get_color_from_hex("#A4A5A6"),
            bold = True,
            font_family="Roboto",
            pos_hint={"center_x":0.5,"center_y":0.85}
        )

        card2 = MDCard(
            size_hint=(1,0.7),
            padding=20,
            radius=[20,20,0,0],
            pos_hint={"x":0,"y":0},
            md_bg_color = get_color_from_hex("#A4A5A6"),
            elevation=5
        )
        signup_label = MDLabel(
            text = "Sign Up",
            text_color=get_color_from_hex("#0C0E0F"),
            theme_text_color="Custom",
            halign="center",
            font_style="H5",
            bold=True,
            pos_hint={"center_x":0.5,"center_y":1}
        )

        user_email = MDLabel(
            text="Email",
            text_color=get_color_from_hex("#0C0E0F"),
            theme_text_color="Custom",
            halign="left",
            font_style="H5",
            bold=True,
            pos_hint={"X":0.07,"center_y":0.85}
        )

        email_input = MDTextField(
            mode="rectangle",
            icon_left="mail",
            text_color_focus= get_color_from_hex("#3B516E"),
            icon_left_color_focus = get_color_from_hex("#3B516E"),
            line_color_focus = get_color_from_hex("#3B516E"),
            pos_hint={"center_x":0.5,"center_y":0.7},
              
        )
        email_otp = MDLabel(
            text="OTP",
            text_color=get_color_from_hex("#0C0E0F"),
            theme_text_color="Custom",
            halign="left",
            font_style="H5",
            bold=True,
            pos_hint={"X":0.07,"center_y":0.55}
        )
        otp_input = MDTextField(
            mode="rectangle",
            icon_left="numeric",
            text_color_focus= get_color_from_hex("#3B516E"),
            icon_left_color_focus = get_color_from_hex("#3B516E"),
            line_color_focus = get_color_from_hex("#3B516E"),
            pos_hint={"center_x":0.5,"center_y":0.42}
        )

        label2 = MDLabel(
            text="Fill Valid information then Go next step !",
            text_color=get_color_from_hex("#0C0E0F"),
            theme_text_color="Custom",
            halign="center",
            font_style="H6",
            bold=True,
            pos_hint={"center_x":0.5,"center_y":0.27}
            
        )

        button = MDRaisedButton(
            text="Next ->",
            pos_hint={"center_x":0.5,"center_y":0.1},
            md_bg_color=get_color_from_hex("#3B516E"),
            theme_text_color = "Custom",
            text_color = get_color_from_hex("#A4A5A6"),
            size_hint=(1,0.1),
            on_release=self.go_to_next
        )

        
        inner_layout = MDFloatLayout()
        inner_layout.add_widget(signup_label)
        inner_layout.add_widget(user_email)
        inner_layout.add_widget(email_input)
        inner_layout.add_widget(email_otp)
        inner_layout.add_widget(otp_input)
        inner_layout.add_widget(label2)
        inner_layout.add_widget(button)
        
        
        card2.add_widget(inner_layout)

        layout.add_widget(card1)
        layout.add_widget(card2)
        layout.add_widget(label1)
        layout.add_widget(back_button)

        self.add_widget(layout)
    def go_to_back(self,*args):
        self.manager.current = "login"

    def go_to_next(self,*args):
        self.manager.current = "user_create"


class new_user_screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = "user_create"

        layout = MDFloatLayout()

        card1 = MDCard(
            size_hint=(1,1),
            md_bg_color=get_color_from_hex("#3B516E"),
        )
        back_button =MDIconButton(
            icon = "arrow-left",
            pos_hint={"center_x":0.08,"center_y":0.92},
            theme_text_color="Custom",
            text_color=get_color_from_hex("#A4A5A6"),
            on_release=self.go_to_back
        )

        label1= MDLabel(
            text = "Herambha",
            font_style = "H4",
            theme_text_color = "Custom",
            halign = "center",
            text_color=get_color_from_hex("#A4A5A6"),
            bold = True,
            font_family="Roboto",
            pos_hint={"center_x":0.5,"center_y":0.85}
        )

        card2 = MDCard(
            size_hint=(1,0.7),
            padding=20,
            radius=[20,20,0,0],
            pos_hint={"x":0,"y":0},
            md_bg_color = get_color_from_hex("#A4A5A6"),
            elevation=5
        )
        signup_label = MDLabel(
            text = "Sign Up",
            text_color=get_color_from_hex("#0C0E0F"),
            theme_text_color="Custom",
            halign="center",
            font_style="H5",
            bold=True,
            pos_hint={"center_x":0.5,"center_y":1}
        )

        user_Name = MDLabel(
            text="User Name",
            text_color=get_color_from_hex("#0C0E0F"),
            theme_text_color="Custom",
            halign="left",
            font_style="H5",
            bold=True,
            pos_hint={"X":0.07,"center_y":0.85}
        )

        username_input = MDTextField(
            mode="rectangle",
            icon_left="account",
            text_color_focus= get_color_from_hex("#3B516E"),
            icon_left_color_focus = get_color_from_hex("#3B516E"),
            line_color_focus = get_color_from_hex("#3B516E"),
            pos_hint={"center_x":0.5,"center_y":0.7},
              
        )
        user_pass = MDLabel(
            text="PassWord",
            text_color=get_color_from_hex("#0C0E0F"),
            theme_text_color="Custom",
            halign="left",
            font_style="H5",
            bold=True,
            pos_hint={"X":0.07,"center_y":0.55}
        )
        pass_input = MDTextField(
            mode="rectangle",
            icon_left="lock",
            text_color_focus= get_color_from_hex("#3B516E"),
            icon_left_color_focus = get_color_from_hex("#3B516E"),
            line_color_focus = get_color_from_hex("#3B516E"),
            pos_hint={"center_x":0.5,"center_y":0.42}
        )

        label2 = MDLabel(
            text="Yeah You Are Valid !",
            text_color=get_color_from_hex("#0C0E0F"),
            theme_text_color="Custom",
            halign="center",
            font_style="H6",
            bold=True,
            pos_hint={"center_x":0.5,"center_y":0.27}
            
        )

        button = MDRaisedButton(
            text="Create User",
            pos_hint={"center_x":0.5,"center_y":0.1},
            md_bg_color=get_color_from_hex("#3B516E"),
            theme_text_color = "Custom",
            text_color = get_color_from_hex("#A4A5A6"),
            size_hint=(1,0.1)
        )

        
        inner_layout = MDFloatLayout()
        inner_layout.add_widget(signup_label)
        inner_layout.add_widget(user_Name)
        inner_layout.add_widget(username_input)
        inner_layout.add_widget(user_pass)
        inner_layout.add_widget(pass_input)
        inner_layout.add_widget(label2)
        inner_layout.add_widget(button)
        
        
        card2.add_widget(inner_layout)

        layout.add_widget(card1)
        layout.add_widget(card2)
        layout.add_widget(label1)
        layout.add_widget(back_button)

        self.add_widget(layout)
    def go_to_back(self,*args):
        self.manager.current = "signup"
        


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        sm = MDScreenManager()
        sm.add_widget(Start_Screen(name="start"))
        sm.add_widget(Login_Screen(name="login"))
        sm.add_widget(signup_Screen(name="signup"))
        sm.add_widget(new_user_screen(name="user_create"))

        
        return sm

if __name__ == "__main__":
    Example().run()