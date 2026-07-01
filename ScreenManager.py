from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.setting import Setting
from screens.theme import Theme
from screens.mainScreen import MainScreen
from screens.testing import Testing
from screens.statictica import Statictic
from screens.exsam import Exsam
from kivy.core.window import Window
from kivy.utils import platform
from screens.config.constants import Constants



if platform in ("win", "linux"):
    Window.minimum_width = Constants.WINDOW_MIN_WIDTH
    Window.minimum_height = Constants.WINDOW_MIN_HEIGHT
    Window.resizeble=True



class MyApp(App):
    
    def build(self):
        sc=ScreenManager()

        sc.add_widget(MainScreen(name="main"))
        sc.add_widget(Theme(name="theme"))
        sc.add_widget(Setting(name="setting"))
        sc.add_widget(Testing(name="testing"))
        sc.add_widget(Exsam(name="exsam"))
        sc.add_widget(Statictic(name="statictic"))
    
        return sc
    
MyApp().run()