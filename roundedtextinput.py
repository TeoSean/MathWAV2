from kivy.lang import Builder
from kivy.uix.textinput import TextInput


Builder.load_file("game.kv")

class RoundedTextInput(TextInput):
    def __init__(self, **kwargs):
        super(RoundedTextInput, self).__init__(**kwargs)

