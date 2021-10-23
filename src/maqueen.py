# -*- coding: utf-8 -*-
""" MaqueenMakeCodeのpythonコードをmicro:bitのmicropythonで動かすためのラーパークラス

Maqueenの制御については、以下のURLを参照しました。
http://oohito.com/nqthm/archives/3116

超音波センサーの実装方法は、以下のURLを参照しました。
https://blog.goo.ne.jp/jh7ubc/e/7d866b2771a6f6282efd70301c79204d

"""
# Micro:bit Maqueen
from microbit import *
from makecode import *
import utime

class PingUnit():
    """ PingUnit enumクラス
    """
    CENTIMETERS = 0
    MICRO_SECONDS = 1

class Maqueen():
    """ Maqueen機能のラッパークラス
    """
    class Dir():
        """ Dir enumクラス
        """
        CW = 0x00
        CCW = 0x01

    class Motors():
        """ Motors enumクラス
        """
        M1 = 0x00
        M2 = 0x02
        ALL = 0xFF

    class LED():
        """ LED enumクラス
        """
        LED_LEFT = pin8
        LED_RIGHT = pin12

    class LEDswitch():
        """ LEDswitch enumクラス
        """
        TURN_ON = 1
        TURN_OFF = 0

    class Patrol():
        """ Patrol enumクラス
        """
        PATROL_LEFT = pin13
        PATROL_RIGHT = pin14

    def __init__(self):
        """ コンストラクタ
        """
        i2c.init()

    def motor_run(self, motor, dir, speed):
        """ 「モータを回す」ブロックのラッパーメソッド

        Args:
            motor (Motors): 回転モーター
            dir: (Dir) 回転方向
            speed: 回転スピード
        """
        i2c.write(16, bytes([motor, dir, speed]))

    def motor_stop(self, motor):
        """ 「モーターを止める」ブロックのラッパーメソッド

        Args:
            motor (Motors): 回転モーター
        """
        if motor == self.Motors.ALL:
            i2c.write(16, bytes([self.Motors.M1, self.Dir.CW, 0]))
            i2c.write(16, bytes([self.Motors.M2, self.Dir.CW, 0]))
        else:
            i2c.write(16, bytes([motor, self.Dir.CW, 0]))
        utime.sleep_ms(10)

    def motor_stop_all(self):
        """ すべてのモータを止める

        古い関数との互換性をとるために定義
        """
        i2c.write(16, bytes([self.aMotors.M1, self.Dir.CW, 0]))
        i2c.write(16, bytes([self.aMotors.M2, self.Dir.CW, 0]))
        utime.sleep_ms(10)

    def write_led(self, pin, value):
        """ 「LEDをつける」ブロックのラッパーメソッド

        Args:
            pin (Pin): LEDのピン
            value (LEDswith): LEDの値
        """
        pin.write_digital(value)

    def read_patrol(self, patrol):
        """ 「ラインセンサーの値」ブロックのラッパーメソッド

        Args:
            patrol (): センサー
        """
        return patrol.read_digital()

    def ultrasonic(self, unit=0):
        """ 「超音波センサーの値」ブロックのラッパーメソッド

        Args:
            unit (PingUnit): 戻り地の単位

        Returns:
            Float: 超音波センサーの値を指定された単位で返す
        """
        pin1.write_digital(0)
        # 音速を計算する
        V = 0.6 * temperature() + 331.5
        # トリガパルス
        pin1.write_digital(1)
        pin1.write_digital(0)
        # 距離の測定と表示
        while pin2.read_digital() == 0:
            utime.sleep_us(1)
        t1 = utime.ticks_us()
        while pin2.read_digital():
            utime.sleep_us(1)
        t2 = utime.ticks_us()
        t = utime.ticks_diff(t2, t1)
        L = int(t * V / 20000)
        if unit == PingUnit.CENTIMETERS:
            return L
        else:
            return t

maqueen = Maqueen()
