from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty


class Widgets(Widget):
    def btn(self):
        show_popup()


class P(FloatLayout):
    pass


class PopUpApp(App):
    def build(self):
        return Widgets()


def show_popup():
    show = P()

    popupwindow = Popup(title='Popup Window', content=show, size_hint=(None, None), size=(300, 300))
    popupwindow.open()


if __name__ == '__main__':
    PopUpApp().run()
