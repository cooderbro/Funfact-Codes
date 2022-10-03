import random as r
import pyautogui as pg
import time

bless=('best',' amazing' ,'great')
time.sleep(4)

for i in range (1000):
     a=r.choice(bless)
     pg.write("You are a " +a)
     pg.press('Enter')