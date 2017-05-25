import pip
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button


print('done installing')


class ConfigWindow(Widget):
    def start_button(self):
        print("JD Powah")


class ConfigApp(App):
    def build(self):
        return ConfigWindow()

ConfigApp().run()