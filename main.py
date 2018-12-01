from time import sleep
import RPi.GPIO as GPIO
from iss_scraping_2 import API

GPIO.setmode(GPIO.BCM)

# Verwendete Pins am Rapberry Pi
A = 18
B = 23
C = 24
D = 25
time = 0.005
home_latitude = 48.0
home_longitude = 11.3
api = API()

# Pins aus Ausgaenge definieren
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.output(A, False)
GPIO.output(B, False)
GPIO.output(C, False)
GPIO.output(D, False)


def step1():
    GPIO.output(D, True)
    sleep(time)
    GPIO.output(D, False)


def step2():
    GPIO.output(D, True)
    GPIO.output(C, True)
    sleep(time)
    GPIO.output(D, False)
    GPIO.output(C, False)


def step3():
    GPIO.output(C, True)
    sleep(time)
    GPIO.output(C, False)


def step4():
    GPIO.output(B, True)
    GPIO.output(C, True)
    sleep(time)
    GPIO.output(B, False)
    GPIO.output(C, False)


def step5():
    GPIO.output(B, True)
    sleep(time)
    GPIO.output(B, False)


def step6():
    GPIO.output(A, True)
    GPIO.output(B, True)
    sleep(time)
    GPIO.output(A, False)
    GPIO.output(B, False)


def step7():
    GPIO.output(A, True)
    sleep(time)
    GPIO.output(A, False)


def step8():
    GPIO.output(D, True)
    GPIO.output(A, True)
    sleep(time)
    GPIO.output(D, False)
    GPIO.output(A, False)


def drehen(schritte):       # Insgesamt 512 schritte
    for i in range(schritte):
        step1()
        step2()
        step3()
        step4()
        step5()
        step6()
        step7()
        step8()


def drehen_rueckwaerts(schritte):       # Insgesamt 512 schritte
    for i in range(schritte):
        step8()
        step7()
        step6()
        step5()
        step4()
        step3()
        step2()
        step1()


def get_winkel_ebene():
    return 0


def get_winkel_hoehe():
    return 0


if __name__ == "__main__":
    akt_winkel_ebene = 0
    akt_winkel_hoehe = 0
    step_const = 512/360
    winkel_const = 360/512
    try:
        while True:

            soll_winkel_ebene, soll_winkel_hoehe = API.get_data()
            schritte_ebene = int((soll_winkel_ebene-akt_winkel_ebene)*step_const)
            akt_winkel_ebene += schritte_ebene*winkel_const
            schritte_hoehe = int((soll_winkel_hoehe-akt_winkel_hoehe)*step_const)
            akt_winkel_hoehe += schritte_hoehe*winkel_const
            sleep(3)
    except KeyboardInterrupt:
        print("\nBeende Programm")
        drehen(512-int(akt_winkel_ebene*step_const))
        GPIO.cleanup()
