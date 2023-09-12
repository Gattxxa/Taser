import os
from PIL import Image
from pynput import mouse
from pystray import Icon, MenuItem, Menu
import sys
import win32gui


PDTH: str = "PAYDAY: The Heist"
PD2: str = "PAYDAY 2"
PD3: str = ""


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def get_active_window_title():
    active_window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(active_window)
    return window_title


def on_scroll(x, y, dx, dy):
    if get_active_window_title() in [PDTH, PD2]:
        mouse_listener.suppress_event()


class Taser:
    def __init__(self, image):
        self.status = False
        text = "Taser (Scroll disabler)"
        icon = Image.open(image)
        menu = Menu(MenuItem("Exit", self.stop_program))
        self.icon = Icon(name=text, title=text, icon=icon, menu=menu)

    def run_program(self):
        mouse_listener.start()
        self.icon.run()

    def stop_program(self):
        mouse_listener.stop()
        self.icon.stop()


if __name__ == "__main__":
    mouse_listener = mouse.Listener(on_scroll=on_scroll)
    system = Taser(image=resource_path("icon.ico"))
    system.run_program()
