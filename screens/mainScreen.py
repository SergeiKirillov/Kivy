from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.setting import Setting
from screens.theme import Theme
from screens.navigator import navigatorMenu

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        blMain = BoxLayout(orientation="vertical")

        lblTitle=Label(text="Главный экрон", color="yellow")
        lblTitle.font_size=28

        #btnTheme=Button(text="Выбор темы заданий",size_hint=(None, None),size=(200,20))
        #btnTheme.id="btn_select_theme"
        #btnTheme.bind(on_release=self.btn_click)

        blMain.add_widget(lblTitle)
        #blMain.add_widget(btnTheme)
        blMain.add_widget(navigatorMenu(self.change_screen))

        self.add_widget(blMain)

    def change_screen(self, screen):
        if screen=="exit":
            App.get_running_app().stop()
        else:
            self.manager.current=screen


#    def btn_click(self, instance):  
#        #print(self.manager.current)
#        self.manager.current = "theme"





    

    

