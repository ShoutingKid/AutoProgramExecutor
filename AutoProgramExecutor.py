import pyautogui as pyauto
import time

time.sleep(0.1)

pyauto.write("cd desktop")
pyauto.press("enter")
time.sleep(0.1)
pyauto.write("cd my projects")
pyauto.press("enter")
time.sleep(0.1)
pyauto.write("cd python")
pyauto.press("enter")
time.sleep(0.1)
pyauto.write("python donut.py")
pyauto.press("enter")
