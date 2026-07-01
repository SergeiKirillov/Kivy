from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def clicker(self, instance):
        if instance.id =="Test":
            instance.disabled=True
            instance.color="red"
            instance.text="Начано тестирование"
        elif instance.id =="Theme":
            instance.text="Редактирование настроек"
        elif instance.id =="Stat":
            instance.text="Отобразить статистику"


    def exit_click(self, instance):
        exit()

    def build(self):
        blMenu=BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20)
        
        blWindowApp=BoxLayout(orientation="horizontal")
        blWimdowMenu=BoxLayout(orientation="vertical")


        lblMenu = Label(text="Меню",color = "blue",font_size=28)
        lblWindowsMenu = Label(text="Окно", font_size=32)

        btnTesting = Button(text="Начать тест",font_size=24)
        btnTesting.bind(on_release=self.clicker)
        btnTesting.id ="Test"
        btnTesting.size_hint=(None,None)
        btnTesting.size=(200,50)

        btnThemeSelect = Button(
            text="Выбор темы",
            font_size=24
            )
        btnThemeSelect.bind(on_release=self.clicker)
        btnThemeSelect.size_hint=(None,None)
        btnThemeSelect.size=(200,50)
        btnThemeSelect.id ="Theme"

        btnStat = Button(
            text="Статистика",
            font_size=24
            )
        btnStat.bind(on_release=self.clicker)
        btnStat.id ="Stat"

        btnExit = Button(
            text="Выход",
            font_size=24
            )
        btnExit.bind(on_release=self.exit_click)
        btnExit.id ="Выход"

        blMenu.add_widget(lblMenu)
        blMenu.add_widget(btnTesting)
        blMenu.add_widget(btnThemeSelect)
        blMenu.add_widget(btnStat)
        blMenu.add_widget(btnExit)

        blWimdowMenu.add_widget(lblWindowsMenu)


        blWindowApp.add_widget(blMenu)
        blWindowApp.add_widget(blWimdowMenu)
        
        return blWindowApp 
    
MyApp().run()
