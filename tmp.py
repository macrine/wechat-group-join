import os
import time
import random


def play():
    while True:
        times = random.randint(5, 15)
        print(times)
        time.sleep(times)
        os.system('adb shell input tap 520 2000')
        times2 = random.randint(3, 6)
        print(times2)
        time.sleep(times2)
        os.system('adb shell input tap 520 2000')


play()
