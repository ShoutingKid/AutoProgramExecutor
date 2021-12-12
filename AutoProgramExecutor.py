import pyautogui as pyauto
import time

time.sleep(1) #you can also change this time

pyauto.write("cd desktop") #specify the directory your file is in
pyauto.press("enter")
time.sleep(0.1) #you can change the time as per your needs
pyauto.write("cd my projects")
pyauto.press("enter")
time.sleep(0.1)
pyauto.write("cd python")
pyauto.press("enter")
time.sleep(0.1)
pyauto.write("python donut.py")
pyauto.press("enter")
