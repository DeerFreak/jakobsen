import RPi.GPIO as GPIO
from time import sleep


class Servo(object):
    def __init__(self, a, b, c, d):
        self.A = a
        self.B = b
        self.C = c
        self.D = d
        self.time = 0.005
        GPIO.setup(self.A, GPIO.OUT)
        GPIO.setup(self.B, GPIO.OUT)
        GPIO.setup(self.C, GPIO.OUT)
        GPIO.setup(self.D, GPIO.OUT)
        GPIO.output(self.A, False)
        GPIO.output(self.B, False)
        GPIO.output(self.C, False)
        GPIO.output(self.D, False)

    def step1(self):
        GPIO.output(self.D, True)
        sleep(self.time)
        GPIO.output(self.D, False)

    def step2(self):
        GPIO.output(self.D, True)
        GPIO.output(self.C, True)
        sleep(self.time)
        GPIO.output(self.D, False)
        GPIO.output(self.C, False)

    def step3(self):
        GPIO.output(self.C, True)
        sleep(self.time)
        GPIO.output(self.C, False)

    def step4(self):
        GPIO.output(self.B, True)
        GPIO.output(self.C, True)
        sleep(self.time)
        GPIO.output(self.B, False)
        GPIO.output(self.C, False)

    def step5(self):
        GPIO.output(self.B, True)
        sleep(self.time)
        GPIO.output(self.B, False)

    def step6(self):
        GPIO.output(self.A, True)
        GPIO.output(self.B, True)
        sleep(self.time)
        GPIO.output(self.A, False)
        GPIO.output(self.B, False)

    def step7(self):
        GPIO.output(self.A, True)
        sleep(self.time)
        GPIO.output(self.A, False)

    def step8(self):
        GPIO.output(self.D, True)
        GPIO.output(self.A, True)
        sleep(self.time)
        GPIO.output(self.D, False)
        GPIO.output(self.A, False)

    def drehen(self, schritte):  # Insgesamt 512 schritte
        for i in range(schritte):
            self.step1()
            self.step2()
            self.step3()
            self.step4()
            self.step5()
            self.step6()
            self.step7()
            self.step8()

    def drehen_rueckwaerts(self, schritte):  # Insgesamt 512 schritte
        for i in range(schritte):
            self.step8()
            self.step7()
            self.step6()
            self.step5()
            self.step4()
            self.step3()
            self.step2()
            self.step1()