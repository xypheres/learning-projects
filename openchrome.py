import webbrowser
import subprocess
import time
import keyboard

webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))

with open("sitelist.txt") as sites:
    sitelist = sites.readlines()

if len(sitelist)>0:
    child = subprocess.Popen("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",shell=True)
    time.sleep(0.5)
    webbrowser.get('chrome').open_new_tab(sitelist[0])
    time.sleep(0.2)

if len(sitelist)>1:
    for i in range(1,len(sitelist)):
        webbrowser.get('chrome').open_new_tab(sitelist[i])
        time.sleep(0.2)

time.sleep(1)
keyboard.press_and_release('ctrl+tab')
time.sleep(1)
keyboard.press_and_release('ctrl+w')