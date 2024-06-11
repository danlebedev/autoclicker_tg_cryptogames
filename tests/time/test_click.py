from tests.tools import check_time
from pyautogui import click
from pynput.mouse import Controller, Button
import mouse
from ahk import AHK


first = (1233, 443)
second = (1475, 296)
third = (1475, 610)


ahk = AHK()
def click_ahk():
    ahk.click(first)
    ahk.click(second)
    ahk.click(third)


def click_mouse():
    mouse.move(*first)
    mouse.click()
    mouse.move(*second)
    mouse.click()
    mouse.move(*third)
    mouse.click()


m = Controller()
def click_pynput():
    m.position = first
    m.click(Button.left)
    m.position = second
    m.click(Button.left)
    m.position = third
    m.click(Button.left)


def click_pg():
    click(*first)
    click(*second)
    click(*third)


check_time(click_mouse, iterations=10)
check_time(click_ahk, iterations=10)
check_time(click_pg, iterations=10)
check_time(click_pynput, iterations=10)
