##

""" MakeCodeのpythonコードをmicro:bitのmicropythonで動かすためのラーパークラス

本ラッパーを使用する場合には、かならず「最初だけ」、「ずっと」ブロックを定義してください。
"""
import microbit as mb

class Basic():
    #--
    def __init__(self):
        mb.compass.heading()

    def forever(self, func):
        #--
        while True:
            global input
            input.checkButtonPressed()
            ##

            if func != None:
                func()

    def pause(self, time):
        #--
        mb.sleep(time)

    def show_string(self, value):
        #--
        mb.display.scroll(value)

    def show_number(self, value):
        #--
        mb.display.scroll(int(value))

    def show_icon(self, icon):
        #--
        mb.display.show(icon)

    def clear_screen(self):
        #--
        mb.display.clear()

class Gesture:
    #--
    SHAKE = "shake"
    LOGO_UP = "up"
    LOGO_DOWN = "down"
    TILT_LEFT = "left"
    TILT_RIGHT = "right"
    SCREEN_UP = "face up"
    SCREEN_DOWN = "face down"
    FREE_FALL = "freefall"

class IconNames(mb.Image):
    #--
    pass

class Button():
    #--
    A = "A"
    B = "B"
    AB = "AB"

class Input():
    #--
    def __init__(self):
        self.buttonFuncs = {}
        self.gestureFuncs = {}

    def temperature(self):
        #--
        return mb.temperature()

    def light_level(self):
        #--
        return mb.display.read_light_level()

    def compass_heading(self):
        #--
        return mb.compass.heading()

    def is_gesture(self, gesture):
        #--
        return mb.accelerometer.is_gesture(gesture)

    def checkButtonPressed(self):
        #--
        btnA_was_pressed = mb.button_a.is_pressed()
        btnB_was_pressed = mb.button_b.is_pressed()
        if Button.AB in self.buttonFuncs and btnA_was_pressed and btnB_was_pressed:
            self.buttonFuncs[Button.AB]()
        elif Button.A in self.buttonFuncs and btnA_was_pressed:
            self.buttonFuncs[Button.A]()
        elif Button.B in self.buttonFuncs and btnB_was_pressed:
            self.buttonFuncs[Button.B]()

    def on_button_pressed(self, button, func):
        #--
        self.buttonFuncs[button] = func

##

basic = Basic()
input = Input()
