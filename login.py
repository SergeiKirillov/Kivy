from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def btnClick(self, instance):
        login=self.txtLogin.text.strip()
        if not login:
            print("Введите логин")
            
        passw=self.txtPassword.text.strip()
        if not passw:
            print("Введите пароль")
            
        else:
            print(f"Пользователь {login} имеет пароль длинной {len(passw)}")




    def build(self):
        blLogin = BoxLayout(orientation="vertical",spacing=10,padding=10)

        lblLoginName = Label(text="Логин", size_hint=(None,None),size=(100,32),font_size=24)
        self.txtLogin = TextInput(hint_text="Введите логин",size_hint=(None,None),size=(400,32),font_size=18)
        self.txtLogin.multiline=False

        lblLoginPassword = Label(text="Пароль",size_hint=(None,None),size=(100,32),font_size=24)
        self.txtPassword=TextInput(hint_text="Введите пароль",size_hint=(None,None),size=(400,32),font_size=18)
        self.txtPassword.multiline=False
        self.txtPassword.password=True
        self.txtPassword.password_mask="#"

        btnSave=Button(text="Сохранить", size_hint=(None,None), size=(400,32), font_size=24)
        btnSave.bind(on_release=self.btnClick)

        blLogin.add_widget(lblLoginName)
        blLogin.add_widget(self.txtLogin)
        blLogin.add_widget(lblLoginPassword)
        blLogin.add_widget(self.txtPassword)
        blLogin.add_widget(btnSave)

        return blLogin
    
MyApp().run()