from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def btnMenuclicker(self, instance):
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
        
        lbTitle=Label(text="Программа по проверки знаний",color = "blue",font_size=28)
        
        lbMenuTitle=Label(text="Меню",color = "white",font_size=18)
        lbMenuTitle.size_hint=(None,None)
        lbMenuTitle.size=(200,50)

        btnMenuTesting = Button(text="Начать тест",font_size=12)
        btnMenuTesting.bind(on_release=self.btnMenuclicker)
        btnMenuTesting.id ="Test"
        btnMenuTesting.size_hint=(None,None)
        btnMenuTesting.size=(200,50)

        btnMenuThemeSelect = Button(text="Выбор темы",font_size=12)
        btnMenuThemeSelect.bind(on_release=self.btnMenuclicker)
        btnMenuThemeSelect.id ="Theme"
        btnMenuThemeSelect.size_hint=(None,None)
        btnMenuThemeSelect.size=(200,50)

        btnMenuStat = Button(text="Статистика",font_size=12)
        btnMenuStat.bind(on_release=self.btnMenuclicker)
        btnMenuStat.size_hint=(None,None)
        btnMenuStat.size=(200,50)
        btnMenuStat.id ="Stat"

        btnMenuExit = Button(text="Выход",font_size=12)
        btnMenuExit.bind(on_release=self.exit_click)
        btnMenuExit.id ="Выход"
        btnMenuExit.size_hint=(None,None)
        btnMenuExit.size=(200,50)

        lbStat=Label(text="Статистика",color = "yellow",font_size=18)

        blWindow=BoxLayout(orientation="vertical")
        bl1 = BoxLayout(orientation="horizontal")
        bl2 = BoxLayout(orientation="horizontal")
        bl3 = BoxLayout(orientation="horizontal")
        blTitle=BoxLayout(orientation="horizontal")
        blMenu=BoxLayout(orientation="vertical")
        blWindowQuestion = BoxLayout(orientation="vertical")
        blStatus=BoxLayout(orientation="horizontal")

        blTitle.add_widget(lbTitle)
        
        blMenu.add_widget(lbMenuTitle)
        blMenu.add_widget(btnMenuTesting)
        blMenu.add_widget(btnMenuThemeSelect)
        blMenu.add_widget(btnMenuStat)
        blMenu.add_widget(btnMenuExit)

        blStatus.add_widget(lbStat)    

        bl1.add_widget(blTitle)
        bl2.add_widget(blMenu)
        bl2.add_widget(blWindowQuestion)
        bl3.add_widget(blStatus)
        
        blWindow.add_widget(bl1)
        blWindow.add_widget(bl2)
        blWindow.add_widget(bl3)

        return blWindow
    
MyApp().run()