from kivymd.uix.backdrop.backdrop import MDFloatLayout
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton,MDRaisedButton,MDTextButton,MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.textfield import MDTextField
from kivy.utils import get_color_from_hex
from kivymd.toast import toast
from mainscreen import home,chatting,all_users
import requests

url = "http://127.0.0.1:5000"

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

        self.user_input = MDTextField(
            
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
        self.pass_input = MDTextField(
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
            size_hint=(1,0.1),
            on_release=self.login_user
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
        inner_layout.add_widget(self.user_input)
        inner_layout.add_widget(user_password)
        inner_layout.add_widget(self.pass_input)
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
    
    def login_user(self,instance):
        login_url = "http://127.0.0.1:5000/user_login"
        user_name = self.user_input.text.strip()
        user_pass = self.pass_input.text.strip()
        if not user_name or not user_pass:
            toast("Fill all textfields")
            return
        data = {
            "user_name" : user_name,
            "user_password" : user_pass
        }
        try:
            resopnse = requests.post(login_url,json=data)
            result = resopnse.json()
            if result["message"] == "User Successfully Login.":
                toast("Login Succssfully")
                self.manager.current = "home"

        except Exception as e:
            toast("There is a problem in login !")
    
    

            

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

        email_layout = MDRelativeLayout(
            size_hint=(1, None),
            height="60dp",
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        )

        self.email_input = MDTextField(
            id="email_field",
            mode="rectangle",
            icon_left="mail",
            text_color_focus= get_color_from_hex("#3B516E"),
            icon_left_color_focus = get_color_from_hex("#3B516E"),
            line_color_focus = get_color_from_hex("#3B516E"),
            pos_hint={"center_x":0.5,"center_y":0.42}
        )

        otp_button = MDFlatButton(
            text="GET OTP",
            pos_hint={"right": 1, "center_y": 0.5},
            on_release=self.send_otp   # your function here
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
        self.otp_input = MDTextField(
            id="OTP_field",
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
            on_release=self.check_otp
        )

        email_layout.add_widget(self.email_input)
        email_layout.add_widget(otp_button)

        inner_layout = MDFloatLayout()
        inner_layout.add_widget(signup_label)
        inner_layout.add_widget(user_email)
        inner_layout.add_widget(email_layout)
        inner_layout.add_widget(email_otp)
        inner_layout.add_widget(self.otp_input)
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
    def send_otp(self,instance):
        email = self.email_input.text

        if not email:
            toast("Enter email first !")
            return
        otp_url = "http://127.0.0.1:5000/verification"

        data = {
            "user_email" : email
        }

        try:
            response = requests.post(otp_url,json=data)
            result = response.json()
            toast(result["message"])
        except Exception as e:
            toast("Server not running !")
    
    def check_otp(self,instance):
        otp_url = "http://127.0.0.1:5000/verification2"
        otp = self.otp_input.text.strip()
        self.email = self.email_input.text.strip()
        
        screen_two = self.manager.get_screen("user_create")
        screen_two.user_email = self.email

        if not otp:
            toast("Enter OTP")
            return
        data = {
            "email" : self.email,
            "otp" : otp
        }

        try:
            response = requests.post(otp_url,json=data)
            result = response.json()

            toast(result["message"])
            if result["message"] == "Email Verified":
                self.go_to_next()

        except Exception as e:
            toast("Server not running")



class new_user_screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user_email = ""

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

        self.username_input = MDTextField(
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
        self.pass_input = MDTextField(
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
            size_hint=(1,0.1),
            on_release=self.create_user
        )

        
        inner_layout = MDFloatLayout()
        inner_layout.add_widget(signup_label)
        inner_layout.add_widget(user_Name)
        inner_layout.add_widget(self.username_input)
        inner_layout.add_widget(user_pass)
        inner_layout.add_widget(self.pass_input)
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
    def create_user(self,instance):
        create_user_url = "http://127.0.0.1:5000/user_create"
        user_name =  self.username_input.text.strip()
        user_pass = self.pass_input.text.strip()
        if not user_name or not user_pass:
            toast("Fill All fileds First !")
            return
        data = {
            "user_email" : self.user_email,
            "user_name" : user_name,
            "user_password" : user_pass
        }
        print(self.user_email)
        try:
            response = requests.post(create_user_url,json=data)
            result = response.json()
            toast(result["message"])
            if result["message"] == "user created successfully.":
                toast("Successfully login !")
                self.go_to_login()
        except Exception as e:
            toast("There is a Problem in Server.")
    
    def go_to_login(self,*args):
        self.manager.current = "login"



        


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        sm = MDScreenManager()
        sm.add_widget(Start_Screen(name="start"))
        sm.add_widget(Login_Screen(name="login"))
        sm.add_widget(signup_Screen(name="signup"))
        sm.add_widget(new_user_screen(name="user_create"))
        sm.add_widget(home(name="home"))
        sm.add_widget(chatting(name="chatting"))
        sm.add_widget(all_users(name="all_users"))

        
        return sm

if __name__ == "__main__":
    Example().run()