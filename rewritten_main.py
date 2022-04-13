from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.clock import Clock
from CustomWidgets import RoundedButton, RoundedTextInput
from kivy.graphics import Rectangle
import time, pyfirmata, sys

class Verifier:
    def __init__(self, port):
        self.board=pyfirmata.Arduino(port)
        self.iterator=pyfirmata.util.Iterator(self.board)
        self.iterator.start()
        time.sleep(0.1)
        self.pin1=self.board.get_pin('d:2:i')
        self.pin2=self.board.get_pin('d:3:i')
        print('ready')
    def check(self):
        running=True
        while running:
            # print((self.pin1.read(), self.pin2.read()))
            if self.pin2.read() == True:
                return 2
            elif self.pin1.read() == True:
                return 1
            time.sleep(0.1)
class Player:
    def __init__(self, name, port):
        self.name=name
        self.port=port
        self.score=0

def rgba(r, g, b, a):
    return (r/255, g/255, b/255, a)

class game_app(App):

    def build(self):
        self.window = FloatLayout()
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.serial_port=sys.argv[1]
        #self.window.spacing = [0, 20]
        Window.clearcolor = rgba(255, 253, 250, 1)
        Window.maximize()
        Clock.schedule_once(self.game)
        self.active_widgets=[]
        return self.window
    def quick_bg(self):
        self.window.clear_widgets()
        self.window.add_widget(
            Image(source='imahes.zip', anim_delay=0, mipmap=True, allow_stretch=True, keep_ratio=False,
                  size_hint=(None, None), size=(self.window.width + 550, self.window.height + 200),
                  pos_hint={'center_x': 0.5, 'center_y': 0.5}))

    def game(self, instance):
        self.window.clear_widgets()

        self.window.add_widget(Image(source='imahes.zip', anim_delay= 0, mipmap= True, allow_stretch= True, keep_ratio=False, size_hint=(None, None), size=(self.window.width+550, self.window.height+200), pos_hint={'center_x': 0.5, 'center_y': 0.5}))

         #self.window.add_widget(Image(source='math_gif_1.gif', anim_delay=0, mipmap=True, allow_stretch=True, keep_ratio=False, size_hint=(None, None), size=(self.window.width + 200, self.window.height + 200), pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        self.window.add_widget(
            Label(text="Simple.", color=(255, 255, 255), font_name="AvenirLTProBlack2.ttf", font_size=45, pos_hint={'center_x': 0.5, 'center_y': 1}))
        self.window.add_widget(
            Label(text="Name of Player 1", color=(255, 255, 255), font_name="AvenirLTProBlack2.ttf", font_size=24, pos_hint={'center_x': 0.5, 'center_y': 0.8}))
        self.player1 = RoundedTextInput(multiline=False, padding=((10, 10, 10, 10)), size_hint=(1, 0.1),
                                        font_name="AvenirLTProBlack2.ttf", cursor_color=(0, 0, 0, 1), font_size=20,
                                        foreground_color=(0, 0, 0, 1), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.player2 = RoundedTextInput(multiline=False, padding=((10, 10, 10, 10)), size_hint=(1, 0.1),
                                        font_name="AvenirLTProBlack2.ttf", cursor_color=(0, 0, 0, 1), font_size=20,
                                        foreground_color=(255, 255, 255), pos_hint={'center_x': 0.5, 'center_y': 0.2})

        self.game_start = RoundedButton(text="Let's Play!", background_color=(212 / 255, 232 / 255, 215 / 255, 0),
                                        size_hint=(1, 0.1), font_size=20, font_name="AvenirLTProBlack2.ttf", pos_hint={'center_x': 0.5, 'center_y': 0})

        self.window.add_widget(self.player1)
        self.window.add_widget(
            Label(text="Name of Player 2", color=(255, 255, 255), font_name="AvenirLTProBlack2.ttf", font_size=24, pos_hint={'center_x': 0.5, 'center_y': 0.4}))
        self.window.add_widget(self.player2)
        self.game_start.bind(on_press=self.start_game)
        self.window.add_widget(self.game_start)

    # def start_game(self, instance):
    #     self.vf=Verifier(self.serial_port)
    #     self.window.clear_widgets()
    #     self.window.add_widget(
    #         Image(source='imahes.zip', anim_delay=0, mipmap=True, allow_stretch=True, keep_ratio=False,
    #               size_hint=(None, None), size=(self.window.width + 550, self.window.height + 200),
    #               pos_hint={'center_x': 0.5, 'center_y': 0.5}))
    #     Clock.schedule_once(self.goto_questions, 0.5)
    # def goto_questions(self, instance):
    #     self.window.clear_widgets()
    #     self.window.add_widget(
    #         Image(source='imahes.zip', anim_delay=0, mipmap=True, allow_stretch=True, keep_ratio=False,
    #               size_hint=(None, None), size=(self.window.width + 550, self.window.height + 200),
    #               pos_hint={'center_x': 0.5, 'center_y': 0.5}))
    #     time.sleep(1)
    #     self.qn_text=Label(text="", color=(255, 255, 255), font_name="AvenirLTProBlack2.ttf", font_size=45, pos_hint={'center_x': 0.5, 'center_y': 1})
    #     self.ans_inp=RoundedTextInput(multiline=False, padding=((10, 10, 10, 10)), size_hint=(1, 0.1),
    #                                     font_name="AvenirLTProBlack2.ttf", cursor_color=(0, 0, 0, 1), font_size=20,
    #                                     foreground_color=(0, 0, 0, 1), pos_hint={'center_x': 0.5, 'center_y': 0.7})
    #     # self.ans_inp=RoundedButton(text="UwU", size_hint=(1, 0.1))
    #     self.ans_button=RoundedButton(text="Submit", background_color=(212 / 255, 232 / 255, 215 / 255, 0),
    #                                     size_hint=(1, 0.1), font_size=20, font_name="AvenirLTProBlack2.ttf", pos_hint={'center_x': 0.5, 'center_y': 0.3})
    #     self.feedback_text=Label(text="", color=(255, 255, 255), font_name="AvenirLTProBlack2.ttf", font_size=24, pos_hint={'center_x': 0.5, 'center_y': 0})
    #     self.window.add_widget(self.ans_button)
    #
    #     self.window.add_widget(self.qn_text)
    #
    #     self.window.add_widget(self.feedback_text)
    #     self.ans_button.bind(on_press=self.verify_test_qn)
    #     Clock.schedule_once(self.test_question, 0.5)
    # def test_question(self, instance):
    #     current_player=None
    #     qn_loop=True
    #     self.qn_text.text='Test Question. Answer is 1'
    #     # if self.vf.check() == 1:
    #     #     current_player=1
    #     # elif self.vf.check() == 2:
    #     #     current_player=2
    # def verify_test_qn(self, instance):
    #     if self.ans_inp.text == 1:
    #         self.feedback_text.text='Correct!'


if __name__ == '__main__':
    game_app().run()