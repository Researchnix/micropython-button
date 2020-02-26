#  Button.py
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

class ButtonTrigger:
    def __init__(self, button):
        self.debug = debug
        self.button = button
        self.current = self.button.value()
        self.rising = []
        self.falling = []
        self.long = []
        self.short = []
        self.continuous= []

    def appendListener(self, method, kind):
        if kind == "rising":
            self.rising.append(method)
        if kind == "falling":
            self.falling.append(method)
        if kind == "long":
            self.long.append(method)
        if kind == "short":
            self.short.append(method)
        if kind == "continuous":
            self.continuous.append(method)

    def buttonCall(self, pin):
        if self._buttonStable():
            self.current = self.button.value()
            if self.button.value() == 1:
                for m in self.falling:
                    m()
            if self.button.value() == 0:
                for m in self.rising:
                    m()
                if self.longPress():
                    for m in self.long:
                        m()
                    self.doContinuously(pin)
                else:
                    for m in self.short:
                        m()

    def doContinuously(self, pin):
        while self.button.value() == 0:
            for m in self.continuous:
                m()
            time.sleep_ms(150)

    def longPress(self):
        for i in range(400):
            if self.button.value() == 1:
                return False
            time.sleep_ms(1)
        return True


    def _buttonStable(self):
        for i in range(10):
            if self.current == self.button.value():
                return False
            time.sleep_ms(1)
        return True
