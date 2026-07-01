from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):
        lblRezume = Label(text="")
        glKeys=GridLayout()
        glKeys.cols=3
        glKeys.padding=10
        glKeys.spacing=5
        glKeys.add_widget(Button(text="1"))
        glKeys.add_widget(Button(text="2"))
        glKeys.add_widget(Button(text="3"))
        glKeys.add_widget(Button(text="4"))
        glKeys.add_widget(Button(text="5"))
        glKeys.add_widget(Button(text="6"))
        glKeys.add_widget(Button(text="7"))
        glKeys.add_widget(Button(text="8"))
        glKeys.add_widget(Button(text="9"))
        glKeys.add_widget(Button(text="0"))
        glKeys.add_widget(Button(text="."))
        glKeys.add_widget(Button(text="="))

        blWindow = BoxLayout(orientation="vertical")
        blWindow.add_widget(lblRezume)
        blWindow.add_widget(glKeys)

        return blWindow
    

MyApp().run()