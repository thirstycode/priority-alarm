import ctypes  # An included library with Python install.
import time

def popup(alarm_text):
    ctypes.windll.user32.MessageBoxW(0, alarm_text, "Alarm Alarm Alarm !!!!", 0)
