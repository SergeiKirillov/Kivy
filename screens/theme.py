from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.setting import Setting
from screens.navigator import navigatorMenu
from kivy.metrics import dp, sp


class Theme(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        blThemeMain=BoxLayout(orientation="vertical")
        blThemeTitle=BoxLayout(orientation="horizontal")
        blThemeSelect=BoxLayout(orientation="vertical")
        
        lblTitle = Label(text="Выбор темы контрольных заданий", color="yellow",font_size=sp(30))
        #lblTitle.size_hint=(None,None)
        #lblTitle.font_size=30
        blThemeTitle.add_widget(lblTitle)

        btnThemeElect = Button(text="Электробезопастность",size_hint=(None,None),size=(dp(400),dp(50)))

        btnThemeElect.id="electr"
        btnThemeElect.bind(on_releas=self.btnThemeSelect_click)

        btnThemeProm = Button(text="Промбезопастность",size_hint=(None,None),size=(dp(400),dp(50)))
        btnThemeProm.id="Prombez"
        btnThemeProm.bind(on_releas=self.btnThemeSelect_click)

        #blThemeSelect.add_widget()
        blThemeSelect.add_widget(btnThemeElect)
        blThemeSelect.add_widget(btnThemeProm)


        blThemeMain.add_widget(blThemeTitle)
        blThemeMain.add_widget(blThemeSelect)
        blThemeMain.add_widget(navigatorMenu(self.change_screen))
       
        self.add_widget(blThemeMain)

    def btn_click(self, instance):  
        #print(self.manager.current)
        self.manager.current = "setting"


    def btnThemeSelect_click(self, instance):
        pass

    def change_screen(self, screen):
        if screen=="exit":
            App.get_running_app().stop()
        else:
            self.manager.current=screen