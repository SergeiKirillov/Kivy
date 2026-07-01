from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.navigator import navigatorMenu
from kivy.metrics import dp,sp


class Exsam(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        blTestingMain=BoxLayout(orientation="vertical")
        blTestingTitle=BoxLayout(orientation="horizontal")
        blTestingQuestion=BoxLayout(orientation="vertical")
        blTestingStatistic=BoxLayout(orientation="horizontal")
        
        lblTitle = Label(text="Экзамен", color="white")
        lblTitle.font_size = sp(30)
        blTestingTitle.add_widget(lblTitle)

        blTestingMain.add_widget(blTestingTitle)
        blTestingMain.add_widget(blTestingQuestion)
        blTestingMain.add_widget(blTestingStatistic)
        blTestingMain.add_widget(navigatorMenu(self.change_screen))
        self.add_widget(blTestingMain)

    def change_screen(self, screen):
        if screen=="exit":
            App.get_running_app().stop()
        else:
            self.manager.current=screen