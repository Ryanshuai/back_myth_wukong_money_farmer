import time

import win32api
import win32con
import pynput

tiaoxi_pos = [745, 422]


class ExecuteCommands():
    def __init__(self):
        self.mouse = pynput.mouse.Controller()
        self.keyboard = pynput.keyboard.Controller()

    def to_position(self):
        print("to position")
        # win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(-1000 * 22), int(0))

        self.keyboard.press(pynput.keyboard.Key.shift)
        self.keyboard.press("w")
        self.keyboard.press("a")
        time.sleep(1.4)
        self.keyboard.release("a")
        self.keyboard.release("w")
        self.keyboard.release(pynput.keyboard.Key.shift)

    def arrow(self):
        print("arrow")
        time.sleep(0.1)
        self.keyboard.tap("1")
        time.sleep(1)
        self.keyboard.tap("f")
        time.sleep(4)

    def back_home(self):
        print("back_home")
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(1000 * 65), int(0))
        self.keyboard.press(pynput.keyboard.Key.shift)
        self.keyboard.press("w")
        time.sleep(1.5)
        self.keyboard.release("w")
        self.keyboard.release(pynput.keyboard.Key.shift)
        time.sleep(0.5)

    def refresh_angle(self):
        print("refresh angle")
        self.keyboard.press("e")
        self.keyboard.release("e")

        self.mouse.position = (tiaoxi_pos[0], tiaoxi_pos[1])

        time.sleep(3)
        self.keyboard.press(pynput.keyboard.Key.enter)
        time.sleep(0.1)
        self.keyboard.release(pynput.keyboard.Key.enter)
        time.sleep(3)

        self.keyboard.press(pynput.keyboard.Key.esc)
        time.sleep(0.1)
        self.keyboard.release(pynput.keyboard.Key.esc)
        time.sleep(1.5)

    def run(self):
        self.refresh_angle()
        self.to_position()
        self.arrow()
        self.back_home()


if __name__ == "__main__":
    time.sleep(2)
    exe = ExecuteCommands()
    while True:
        exe.run()
