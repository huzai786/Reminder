import os
from typing import NamedTuple

import pyautogui as pg
import schedule


class Job(NamedTuple):
    time: str
    reminder: str


class Person:
    def __init__(self, number):
        assert type(number) is str
        self.number = str(number)

    def call(self, msg):
        pg.press('win')
        pg.sleep(1)
        pg.write('WhatsApp')
        pg.sleep(2)
        r = None
        while r is None:
            r = pg.locateCenterOnScreen(os.path.join(os.getcwd(), 'images', 'watsapp.png'),
                                        grayscale=True, confidence=.5)

        pg.moveTo(r[0], r[1])
        pg.click()

        while True:
            opened = pg.locateCenterOnScreen(os.path.join(os.getcwd(), 'images', 'chat.png'),
                                        grayscale=True, confidence=.5)
            if opened:
                break

        # opening persons tab
        pg.hotkey('ctrl', 'f')
        pg.write(self.number)
        pg.sleep(2)
        pg.press('down')
        pg.sleep(2)
        pg.press('enter')
        pg.sleep(1)

        # send msg
        pg.write(msg)
        pg.sleep(1)
        pg.press('enter')
        pg.sleep(1)

        # call
        pg.click(1485, 101)
        pg.sleep(5)

        # cancel call
        pg.click(895, 705)
        pg.sleep(3)
        pg.click(800, 450)
        pg.hotkey('alt', 'f4')


class Schedular:
    def __init__(self, person: Person, *args):
        self.person = person
        self.jobs = args

    def schedule_reminder(self):
        for job in self.jobs:
            schedule.every().day.at(job.time).do(self.person.call, job.reminder)