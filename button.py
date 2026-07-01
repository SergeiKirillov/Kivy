from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyAppButton(App):
    def clicked(self, instance):
        if instance.text=="Начать тест":
            instance.text="Тест запущен"
            instance.disabled = True
        elif instance.text=="Сообщение":
            print("Вторая кнопка")
    

    def build(self):

        layout1 = BoxLayout(orientation="vertical")

        lbl1 = Label(text="Урок 5")

        btn1 = Button(text="Начать тест")
        btn1.bind(on_release=self.clicked)

        btn2 = Button(text="Сообщение")
        btn2.bind(on_release=self.clicked)

        layout1.add_widget(lbl1)
        layout1.add_widget(btn1)
        layout1.add_widget(btn2)

        return layout1
    


MyAppButton().run()

    
    