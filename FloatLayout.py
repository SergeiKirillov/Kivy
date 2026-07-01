from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        flWindow= FloatLayout()

        btn = Button()
        btn.text="Кнопка"
        btn.size_hint=(None,None)
        btn.size=(200,50)
        btn.pos_hint={"y":0,"center_x":0.5}

        flWindow.add_widget(Button(text="1", size_hint=(None,None), size=(100,50), pos_hint={"x":0,"center_y":0.5}))
        flWindow.add_widget(Button(text="2", size_hint=(None,None), size=(100,50), pos_hint={"center_x":0.5,"top":1}))
        flWindow.add_widget(Button(text="3", size_hint=(None,None), size=(100,50), pos_hint={"right":1,"center_y":0.5}))
        flWindow.add_widget(btn)
        return flWindow
    


MyApp().run()