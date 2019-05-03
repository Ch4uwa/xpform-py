import kivy

kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class MyFloatApp(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    MyFloatApp().run()
