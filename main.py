
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.clock import Clock
from CustomWidgets import RoundedButton, RoundedTextInput
from kivy.graphics import Rectangle
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import time, pyfirmata

Builder.load_file("game.kv")

class RoundedTextInput(TextInput):
    def __init__(self, **kwargs):
        super(RoundedTextInput, self).__init__(**kwargs)

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)



class Player:
    def __init__(self,name, port):
        self.name=name
        self.port=port
        self.score=0
def rgba(r, g, b, a):
    return (r/255, g/255, b/255, a)
class game_app(App):
    def build(self):

        self.window = GridLayout()

        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.window.spacing=[0, 20]

        #Window.clearcolor = (235/255, 113/255, 174/255, 1)
        Window.clearcolor=rgba(255, 253, 250, 0.5)
        self.bg=Rectangle(pos=self.window.pos, size=self.window.size)
        self.bg.source="bg.png"
        self.window.canvas.draw()
        self.qn_bitmaps=[]
        Clock.schedule_once(self.game, 0.5)
        Window.maximize()
        return self.window

    def game(self, instance):
        self.window.clear_widgets()
        #self.window2.add_widget(Image(source='math_gif_1.gif', anim_delay=0, mipmap=True, allow_stretch=True, keep_ratio=False, size_hint=(None, None), size=(self.window.width + 200, self.window.height + 200), pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        self.window.add_widget(Label(text="Simple.", color=(255, 255, 255), font_name="AvenirLTProBlack2.ttf", font_size=45))
        self.window.add_widget(Label(text="Name of Player 1", color=(255, 255, 255), font_name="AvenirLTProBlack2.ttf", font_size=24))
        self.player1 = RoundedTextInput(multiline=False, padding=((10, 10, 10, 10)), size_hint=(0.9, 0.7), font_name="AvenirLTProBlack2.ttf", cursor_color=(0, 0, 0, 1), font_size=20, foreground_color=(0, 0, 0, 1))
        self.player2 = RoundedTextInput(multiline=False, padding=((10, 10, 10, 10)), size_hint=(0.9, 0.7), font_name="AvenirLTProBlack2.ttf", cursor_color=(0, 0, 0, 1),font_size=20, foreground_color=(255, 255, 255))

        self.game_start = RoundedButton(text="Let's Play!", background_color=(212/255, 232/255, 215/255, 0), size_hint=(1, 0.8), font_size=20, font_name="AvenirLTProBlack2.ttf")

        self.game_start.bind(on_press=self.goto_check)
        self.error_message = Label(text="", color=(1, 0, 0, 1), font_name="AvenirLTProBlack2.ttf", font_size=20)
        self.window.add_widget(self.player1)
        self.window.add_widget(Label(text="Name of Player 2", color=(255, 255, 255), font_name="AvenirLTProBlack2.ttf", font_size=24))
        self.window.add_widget(self.player2)
        self.window.add_widget(self.game_start)
        self.window.add_widget(self.error_message)





    def goto_check(self, instance):
        if self.player1.text == "" or self.player2.text == "":
            self.error_message.text="Please enter both Player 1 and Player 2's names!"
        else:
            self.window.clear_widgets()

            self.window.add_widget(Label(text="Please enter the serial port of the Arduino!", font_name="AvenirLTProBlack2.ttf", font_size=40, color=(0, 0, 0, 1)))
            self.port=RoundedTextInput(multiline=False, padding_y=(10, 10), size_hint=(1, 0.5), font_name="AvenirLTProBlack2.ttf", font_size=20)
            self.window.add_widget(self.port)
            self.submit_port=RoundedButton(text="Check", background_color=(0, 0, 0, 0), font_name="AvenirLTProBlack2.ttf", size_hint=(1, 0.7), font_size=30)
            self.window.add_widget(self.submit_port)
            self.incorrect_port=Label(text="", color=(1, 0, 0, 1))
            self.window.add_widget(self.incorrect_port)
            self.submit_port.bind(on_press=self.check_port)

    def check_port(self, instance):
        try:
            self.incorrect_port.color=(0, 0, 0, 1)
            self.incorrect_port.text="Initiating port test..."
            self.arduino=pyfirmata.Arduino(self.port.text)
            self.iterator=pyfirmata.util.Iterator()
            self.iterator.start()
            print("Port test succeeded")
            self.incorrect_port.text="Port correct!"
            self.incorrect_port.color=(0, 1, 0, 1)
            self.player1=Player(self.player1, self.arduino.get_pin('d:3:i'))
            self.player2 = Player(self.player2, self.arduino.get_pin('d:4:i'))
            Clock.schedule_once(self.begin_game, 0.5)
        except:
            self.incorrect_port.color = (1, 0, 0, 1)
            self.incorrect_port.text="Incorrect Port!"
            Clock.schedule_once(self.goto_check, 0.5)


    def begin_game(self, instance):
        self.window.clear_widgets()







if __name__ == "__main__":
    game_app().run()
