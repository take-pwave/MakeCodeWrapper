# -*- coding: utf-8 -*-
""" MakeCodeのpythonコードをmicro:bitのmicropythonで動かすためのラーパークラス

本ラッパーを使用する場合には、かならず「最初だけ」、「ずっと」ブロックを定義してください。
"""
import microbit as mb

class Basic():
    """ Basic機能のラッパークラス

    Micro:bitの基本機能を実装します。
    ラーパークラスがmicropythonのディスクスペースを圧迫しないように、
    Basicブロックのすべての機能を実装するのではなく、必要最低限とします。

    未実装ブロックは、「LED画面に表示」、「矢印を表示」です。
    """
    def __init__(self):
        mb.compass.heading()

    def forever(self, func):
        """ 「ずっと」ブロックのラッパーメソッド

        Args:
            func (function): 「ずっと」処理で実行する関数

        """
        while True:
            global input
            input.checkButtonPressed()
            # ユーザ定義関数の実行
            if func != None:
                func()

    def pause(self, time):
        """ 「一時停止(ミリ秒)」ブロックのラッパーメソッド

        Args:
            time (int): 停止時間をミリ秒で指定
        """
        mb.sleep(time)

    def show_string(self, value):
        """ 「文字列を表示」  
              
        Args:
            value (String): 表示する文字列
        """
        mb.display.scroll(value)

    def show_number(self, value):
        """ 「数を表示」ブロックのラッパーメソッド

        Args:
            value (int): 表示する数値
        """
        mb.display.scroll(int(value))

    def show_icon(self, icon):
        """ 「アイコンを表示」ブロックのラッパーメソッド

        Args:
            icon (IconNames): アイコン名
        """
        mb.display.show(icon)

    def clear_screen(self):
        """ 「表示を消す」ブロックのラッパーメソッド
        """
        mb.display.clear()

class Gesture:
    """ Gesture enumクラス

    3G, 6G, 8Gは省略した。
    """
    SHAKE = "shake"
    LOGO_UP = "up"
    LOGO_DOWN = "down"
    TILT_LEFT = "left"
    TILT_RIGHT = "right"
    SCREEN_UP = "face up"
    SCREEN_DOWN = "face down"
    FREE_FALL = "freefall"

class IconNames(mb.Image):
    """ microbit.Imageからアイコン名を利用するためのサブクラス
    """
    pass

class Button():
    """ Button enumクラス
    """
    A = "A"
    B = "B"
    AB = "AB"

class Input():
    """ 「入力」機能のラッパークラス

    未実装は、「ゆさぶられたとき」、「端子が短くタップされたとき」、「加速度」、「端子がタッチされている」
    """
    def __init__(self):
        self.buttonFuncs = {}
        self.gestureFuncs = {}

    def temperature(self):
        """ 「温度」ブロックのラッパーメソッド
        温度を返す

        Returns:
            Float: 温度
        """
        return mb.temperature()

    def light_level(self):
        """ 「明るさ」ブロックのラッパーメソッド

        LED画面に当たる光の明るさを返す

        Returns:
            int: 明るさ（0:暗いから255:明るいの範囲）
        """
        return mb.display.read_light_level()

    def compass_heading(self):
        """ 「方角」ブロックのラッパーメソッド

        現在のコンパスの値を返す
        Returns:
            Int: 方角
        """
        return mb.compass.heading()

    def is_gesture(self, gesture):
        """ 「動き」ブロックのラッパーメソッド

        指定された動きか否かを返す

        Returns:
            Bool: True: 指定された動きの場合、それ以外　False

        """
        return mb.accelerometer.is_gesture(gesture)

    def checkButtonPressed(self):
        """ ボタン押下のチェック

        登録されているボタン押下がある場合には、そのコールバック関数を実行する        
        """
        btnA_was_pressed = mb.button_a.is_pressed()
        btnB_was_pressed = mb.button_b.is_pressed()
        if Button.AB in self.buttonFuncs and btnA_was_pressed and btnB_was_pressed:
            self.buttonFuncs[Button.AB]()
        elif Button.A in self.buttonFuncs and btnA_was_pressed:
            self.buttonFuncs[Button.A]()
        elif Button.B in self.buttonFuncs and btnB_was_pressed:
            self.buttonFuncs[Button.B]()

    def on_button_pressed(self, button, func):
        """ 「ボタンが押されたとき」ブロックのラッパーメソッド

        指定されたボタン（button）が押されたときに実行するコールバック関数（func）を登録する

        Args:
            button (Button enum): ボタン種別
            func (コールバック関数): ボタン押下時のコールバック関数
        """
        self.buttonFuncs[button] = func

# import先で利用する変数
basic = Basic()
input = Input()
