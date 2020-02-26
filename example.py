#  example.py
#  micropython-button
#
#  Initial Version January 2020
#  Latest Update January 2020
#  Version 1.0.0
#
#  Ceated on 12 January 2020 by
#  Lennart Doppenschmitt     https://github.com/researchnix
#  Rene Vollmer              https://github.com/aypac
#
#  MIT License
#  Copyright (c) 2020 Lennart


import time
import sys
import Button
from machine import PWM
from machine import Pin


triggerActive = False
led = PWM(Pin(4))
led.duty(0)


def toggleLed():
    if led.duty() == 0:
        led.duty(100)
    else:
        led.duty(0)

def increaseLed():
    c = led.duty()
    c = (c + 20) % 200
    led.duty(c)

but = Pin(5, Pin.IN, Pin.PULL_UP)
trig = Button.ButtonTrigger(but)
trig.appendListener(toggleLed, "short")
trig.appendListener(increaseLed, "continuous")
but.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler= trig.buttonCall)
