from time import sleep
import RPi.GPIO as GPIO
from iss_scraping_2 import API
from servo import Servo

GPIO.setmode(GPIO.BCM)

# Verwendete Pins am Rapberry Pi
servo1 = Servo(18, 23, 24, 25)
servo2 = Servo(4, 17, 27, 22)
home_latitude = 48.0
home_longitude = 11.3
api = API()


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
            if schritte_ebene >= 0:
                servo1.drehen(schritte_ebene)
            else:
                servo1.drehen_rueckwaerts(-schritte_ebene)
            schritte_hoehe = int((soll_winkel_hoehe-akt_winkel_hoehe)*step_const)
            akt_winkel_hoehe += schritte_hoehe*winkel_const
            if schritte_hoehe >= 0:
                servo2.drehen(schritte_hoehe)
            else:
                servo2.drehen_rueckwaerts(-schritte_hoehe)
            sleep(3)
    except KeyboardInterrupt:
        print("\nBeende Programm")
        servo1.drehen(512-int(akt_winkel_ebene*step_const))
        servo2.drehen(512-int(akt_winkel_hoehe*step_const))
        GPIO.cleanup()
