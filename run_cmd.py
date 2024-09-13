import time

import win32api
import win32con
import pynput

tiaoxi_pos = [745, 422]


class ExecuteCommands():
    def __init__(self):
        self.mouse = pynput.mouse.Controller()
        self.keyboard = pynput.keyboard.Controller()

    def back_home(self):
        print("back_home")
        self.keyboard.press(pynput.keyboard.Key.esc)
        time.sleep(0.1)
        self.keyboard.release(pynput.keyboard.Key.esc)
        time.sleep(1)

        self.keyboard.press("d")
        time.sleep(0.1)
        self.keyboard.release("d")

        self.keyboard.press(pynput.keyboard.Key.enter)
        time.sleep(0.1)
        self.keyboard.release(pynput.keyboard.Key.enter)

        time.sleep(0.5)

        self.keyboard.press(pynput.keyboard.Key.enter)
        time.sleep(0.1)
        self.keyboard.release(pynput.keyboard.Key.enter)

        time.sleep(0.5)

        self.keyboard.press(pynput.keyboard.Key.enter)
        time.sleep(0.1)
        self.keyboard.release(pynput.keyboard.Key.enter)
        time.sleep(17)

    def to_position(self):
        print("to position")

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(1000 * 70), int(0))

        self.keyboard.press(pynput.keyboard.Key.shift)
        self.keyboard.press("w")
        time.sleep(2)
        self.keyboard.release("w")
        self.keyboard.release(pynput.keyboard.Key.shift)

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -int(1000 * 35), int(0))

        self.keyboard.press(pynput.keyboard.Key.shift)
        self.keyboard.press("w")
        time.sleep(2.5)
        self.keyboard.release("w")
        self.keyboard.release(pynput.keyboard.Key.shift)

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -int(1000 * 15), int(0))

        self.keyboard.press(pynput.keyboard.Key.shift)
        self.keyboard.press("w")
        time.sleep(3)
        self.keyboard.release("w")
        self.keyboard.release(pynput.keyboard.Key.shift)

    def explode(self):
        print("explode")
        time.sleep(1)

        time.sleep(0.1)
        self.keyboard.press("4")
        time.sleep(0.1)
        self.keyboard.release("4")
        time.sleep(1.5)
        self.keyboard.press("4")
        time.sleep(0.1)
        self.keyboard.release("4")

        time.sleep(5)

    def refresh_angle(self):
        print("refresh angle")
        self.keyboard.press("e")
        self.keyboard.release("e")

        time.sleep(3)

        # mouse.position = (tiaoxi_pos[0], tiaoxi_pos[1])
        # print("click left")
        # mouse.click(pynput.mouse.Button.left)
        # time.sleep(3)

        self.keyboard.press(pynput.keyboard.Key.esc)
        time.sleep(0.1)
        self.keyboard.release(pynput.keyboard.Key.esc)

        time.sleep(2)


    def run(self):
        self.backhome()
        self.refresh_angle()
        self.to_position()
        self.explode()


if __name__ == "__main__":
    time.sleep(2)
    exe = ExecuteCommands()
    while True:
        exe.run()
