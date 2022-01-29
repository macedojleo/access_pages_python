import webbrowser
import time
import pyautogui
from datetime import datetime

def access_page(url, time_sleep):
    now = datetime.now()
    print("Open " + url, now)
    webbrowser.open(url)
    time.sleep(time_sleep)
    pyautogui.hotkey('ctrl', 'w')
    print("Closing page")

while True:
    with open('lista.txt') as f:
        line = f.readline()
        while line:
            line = f.readline()
            access_page(line, 210)
    time.sleep(5)