import win32api
import win32con
import win32gui
import time

class MouseControler:

    def get_screen_size(self):
        return (
            win32api.GetSystemMetrics(win32con.SM_CXSCREEN),
            win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        )

    def move_mouse(x_offset, y_offset):
        x, y = MouseControler.get_mouse_position()
        win32api.SetCursorPos((x + int(x_offset), y + int(y_offset)))

    def get_mouse_position():
        return win32api.GetCursorPos()
    
    
    def mouse_click(x: int|None = None, y: int|None = None):
        if x is not None and y is not None:
            MouseControler.move_mouse(x,y)

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    