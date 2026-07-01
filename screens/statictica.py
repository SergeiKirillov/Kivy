from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.navigator import navigatorMenu


class Statictic(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        blStatisticMain=BoxLayout(orientation="vertical")
        blStatisticSelect=BoxLayout(orientation="vertical")
        
        lblStatisticTitle=Label(text="Экрон статистик", color="yellow") 
        btnStatisticMenu = Button(text="Назад в Меню",size_hint=(None, None),size=(200,20))
        blStatisticSelect.add_widget(lblStatisticTitle)
        blStatisticSelect.add_widget(btnStatisticMenu)
        
        blStatisticMain.add_widget(blStatisticSelect)
        blStatisticMain.add_widget(navigatorMenu())

        
        self.add_widget(blStatisticMain)