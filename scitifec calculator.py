import random

import pyautogui as pg
import time
animal = ('monkey', 'donkey','dog')
time.sleep(5)

for i in range(400):
    a = random.choice(animal)
    pg.write("you are a "+a)
    pg.press('enter')

