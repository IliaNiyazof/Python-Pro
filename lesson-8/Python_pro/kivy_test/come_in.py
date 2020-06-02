import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')
Config.set('graphics', 'resizable', '0')


class AppKivy(App):

    def build(self):
        al = AnchorLayout()

        bl = BoxLayout(orientation='vertical', size_hint=[.5, .5])
        bl.add_widget(Label(text='Логин', size_hint=[None, None], size=[150, 30]))
        bl.add_widget(TextInput(size_hint=[None, None], size=[150, 30]))
        bl.add_widget(Label(text='Пароль', size_hint=[None, None], size=[150, 30]))
        bl.add_widget(TextInput(size_hint=[None, None], size=[150, 30]))

        bl.add_widget(Button(text='Войти', size_hint=[None, None], size=(150, 30)))

        al.add_widget(bl)
        return al


if __name__ == '__main__':
    AppKivy().run()
