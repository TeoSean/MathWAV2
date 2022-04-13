from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import time
class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.4, 0.3)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        Window.clearcolor = (1, 1, 1)
        self.window.add_widget(Label(text="Name of Player 1", color=(255, 255, 255)))
        self.player1=TextInput(multiline=False,padding_y=(20, 20), size_hint=(1, 1))
        self.player2 = TextInput(multiline=False, padding_y=(20, 20), size_hint=(1, 1))
        self.window.add_widget(self.player1)
        self.window.add_widget(self.player2)
        return self.window

SayHello().run()