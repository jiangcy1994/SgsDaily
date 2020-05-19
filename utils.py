import time
import win32api, win32con

__all__ = ['lbtton_click_wait', 'send_input_wait', 'default_wait_interval']

default_wait_interval = 3

def lbtton_click(handle, x, y):
    win32api.PostMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
    win32api.PostMessage(handle, win32con.WM_LBUTTONUP, 0, win32api.MAKELONG(x, y))

def send_input(handle, msg):
    for c in msg:
        if c == "\n":
            win32api.PostMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
            win32api.PostMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        else:
            win32api.PostMessage(handle, win32con.WM_CHAR, ord(c), 0)

def lbtton_click_wait(handle, x, y, wait_time=default_wait_interval):
    lbtton_click(handle, x, y)
    time.sleep(wait_time)

def send_input_wait(handle, msg, wait_time=default_wait_interval):
    send_input(handle, msg)
    time.sleep(wait_time)
