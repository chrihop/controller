#!/usr/bin/env python3

import smbus
import RPi.GPIO as GPIO
import time

class Motor:
    I2C_BUS_ID = 1
    bus = None
    def __init__(self):
        self.bus = smbus.SMBus(I2C_BUS_ID)
        pass

    def start(self):
        self.bus.write_byte_data(0x20, 0x06, 0x00)
        return True

    def set_target_speed(self, channel, speed):
        pass

class RemoteControl:
    def __init__(self):
        pass

    @staticmethod
    def on_signal(self):
        pass

    def start(self):
        GPIO.add_event_detect(25, GPIO.FALLING, callback=on_signal)
        return True

    def read_command(self):
        pass


class MainLoop:
    rc = None
    motor = None

    def __init__(self):
        self.rc = RemoteControl()
        self.motor = Motor()
        pass

    def start(self):
        if not self.rc.start():
            return False
        if not self.motor.start():
            return False
        return True

    def spin(self):
        pass

class Main:

    @staticmethod
    def main():
        controller = MainLoop()
        if controller.start():
            print("drone started.")
            controller.spin()
        else:
            print("drone start failed.\n")

Main.main()






