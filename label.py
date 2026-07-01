from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Изучаю Kivy\nsergeiakir ", font_size=32, color="red")
    
MyApp().run()
    