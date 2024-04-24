from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import json
# #?مكتبة اللغة العربية
# import arabic_reshaper
# #?لعكس الحروف العربية
# import bidi.algorithm
    
class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.padding = [50, 20]
        self.spacing = 10
        # username = arabic_reshaper.reshape('اسم المستخدم')
        # bidi_username = bidi.algorithm.get_display(username)
        # self.username_input = TextInput(hint_text= bidi_username, font_name='Arial')
        self.username_input = TextInput(hint_text= "User Name", font_name='Arial')

        # password = arabic_reshaper.reshape('كلمة المرور')
        # bidi_password = bidi.algorithm.get_display(password)
        # self.password_input = TextInput(hint_text=bidi_password, password=True, font_name='Arial')
        self.password_input = TextInput(hint_text="Password", password=True, font_name='Arial')
        
        # login = arabic_reshaper.reshape('تسجيل الدخول')
        # bidi_login = bidi.algorithm.get_display(login)
        # self.login_button = Button(text=bidi_login,font_name='Arial')
        self.login_button = Button(text="Singin",font_name='Arial')
        self.login_button.bind(on_press=self.login)

        # singin = arabic_reshaper.reshape('إنشاء حساب') 
        # bidi_singin = bidi.algorithm.get_display(singin)
        # self.signup_button = Button(text=bidi_singin ,font_name='Arial')
        self.signup_button = Button(text="Singup" ,font_name='Arial')
        self.signup_button.bind(on_press=self.signup)


        # labl = arabic_reshaper.reshape('مرحبًا بك في برنامج تسجيل الدخول')
        # bidi_labl = bidi.algorithm.get_display(labl)
        # self.add_widget(Label(text=bidi_labl, font_size='20sp',font_name='Arial'))
        self.add_widget(Label(text="Welcome to Login App", font_size='20sp',font_name='Arial'))
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)
        self.add_widget(self.login_button)
        self.add_widget(self.signup_button)

        # labl2 = arabic_reshaper.reshape("حالة التسجيل")
        # bidi_labl2 = bidi.algorithm.get_display(labl2)
        # self.Label2 = Label(text=bidi_labl2, font_size='18sp',font_name='Arial')
        self.Label2 = Label(text="Login&Singup State", font_size='18sp',font_name='Arial')
        self.add_widget(self.Label2)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        with open('D:\\LearnPython\\Kivy\\add acount\\users.json', 'r') as file:
            users = json.load(file)
        if username in users and users[username] == password:
            # Label2 = arabic_reshaper.reshape("تم تسجيل الدخول بنجاح")
            # bidi_Label2 = bidi.algorithm.get_display(Label2)
            # self.Label2.text = bidi_Label2
            self.Label2.text = "Succes Login"
            self.Label2.color = 'green'            
        else:
            # Label2 = arabic_reshaper.reshape("اسم المستخدم أو كلمة المرور غير صحيحة")
            # bidi_Label2 = bidi.algorithm.get_display(Label2)
            # self.Label2.text = bidi_Label2
            self.Label2.text = "Wrong with Username Or Password"
            self.Label2.color = 'red' 
    def signup(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        with open('D:\\LearnPython\\Kivy\\add acount\\users.json', 'r') as file:
            users = json.load(file)
        if (username in users):
            # Label2 = arabic_reshaper.reshape("اسم المستخدم موجود بالفعل")
            # bidi_Label2 = bidi.algorithm.get_display(Label2)
            # self.Label2.text = bidi_Label2
            self.Label2.text = "Username Found"
            self.Label2.color = 'red' 
        elif (username and password != ''):
            users[username] = password
            with open('D:\\LearnPython\\Kivy\\add acount\\users.json', 'w') as file:
                json.dump(users, file)
            # Label2 = arabic_reshaper.reshape("تم إنشاء الحساب بنجاح")
            # bidi_Label2 = bidi.algorithm.get_display(Label2)
            # self.Label2.text = bidi_Label2
            self.Label2.text = "Succec Creat Acount"
            self.Label2.color = 'green'
        else:
            # Label2 = arabic_reshaper.reshape("تأكد من الكتابة بشكل صحيح")
            # bidi_Label2 = bidi.algorithm.get_display(Label2)
            # self.Label2.text = bidi_Label2
            self.Label2.text = "Check Input"
            self.Label2.color = 'red' 
        

class LoginApp(App):
    def build(self):
        self.title = "برنامج تسجيل الدخول"
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
