# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 19:40:03 2022

@author: Alice
"""

import pywinauto

# get list of open windows for troubleshooting
windows = pywinauto.Desktop(backend="uia").windows()
for w in windows:
    print(w.window_text())

def init_windows():
    terminal_app = pywinauto.application.Application().connect(title_re=".*(anaconda3)")
    firefox_app = pywinauto.application.Application().connect(title_re=".*Firefox")

    terminal_window = terminal_app.window()
    firefox_window = firefox_app.window()

    return terminal_window, firefox_window

def send_raspi_command(terminal_window, firefox_window):
    terminal_window.set_focus()
    pywinauto.keyboard.send_keys('python{SPACE}run_motors.py{ENTER}')
    firefox_window.set_focus()

if __name__ == "__main__":
    firefox_window, terminal_window = init_windows()
    send_raspi_command(firefox_window, terminal_window)