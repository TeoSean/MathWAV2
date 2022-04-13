from kivy.lang import Builder

from kivy.uix.button import Button

Builder.load_file("game.kv")

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)