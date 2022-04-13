from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


Builder.load_file("game.kv")



class RoundedTextInput(TextInput):
    def __init__(self, **kwargs):
        super(RoundedTextInput, self).__init__(**kwargs)

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)

