##

""" MaqueenMakeCodeのpythonコードをmicro:bitのmicropythonで動かすためのラーパークラス

Maqueenの制御については、以下のURLを参照しました。
http://oohito.com/nqthm/archives/3116

"""
##

from microbit import *
from makecode import *
import utime

class PingUnit():
    #--
    CENTIMETERS = 0
    MICRO_SECONDS = 1

class Maqueen():
    #--
    class Dir():
        #--
        CW = 0x00
        CCW = 0x01

    class Motors():
        #--
        M1 = 0x00
        M2 = 0x02
        ALL = 0xFF

    class LED():
        #--
        LED_LEFT = pin8
        LED_RIGHT = pin12

    class LEDswitch():
        #--
        TURN_ON = 1
        TURN_OFF = 0

    class Patrol():
        #--
        PATROL_LEFT = pin13
        PATROL_RIGHT = pin14

    def __init__(self):
        #--
        i2c.init()

    def motor_run(self, motor, dir, speed):
        #--
        i2c.write(16, bytes([motor, dir, speed]))

    def motor_stop(self, motor):
        #--
        if motor == self.Motors.ALL:
            i2c.write(16, bytes([self.Motors.M1, self.Dir.CW, 0]))
            i2c.write(16, bytes([self.Motors.M2, self.Dir.CW, 0]))
        else:
            i2c.write(16, bytes([motor, self.Dir.CW, 0]))
        utime.sleep_ms(10)

    def motor_stop_all(self):
        #--
        i2c.write(16, bytes([self.aMotors.M1, self.Dir.CW, 0]))
        i2c.write(16, bytes([self.aMotors.M2, self.Dir.CW, 0]))
        utime.sleep_ms(10)

    def write_led(self, pin, value):
        #--
        pin.write_digital(value)

    def read_patrol(self, patrol):
        #--
        return patrol.read_digital()

    def ultrasonic(self, unit=0):
        #--
        pin1.write_digital(0)
        ##

        V = 0.6 * temperature() + 331.5
        ##

        pin1.write_digital(1)
        pin1.write_digital(0)
        ##

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
