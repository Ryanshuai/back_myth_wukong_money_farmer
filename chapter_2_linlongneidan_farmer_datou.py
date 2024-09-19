import time

import win32api
import win32con
import pynput

tiaoxi_pos = [745, 422]


class ExecuteCommands():
    def __init__(self):
        self.mouse = pynput.mouse.Controller()
        self.keyboard = pynput.keyboard.Controller()

    def forward(self, duration):
        print("forward")
        self.keyboard.press(pynput.keyboard.Key.shift)
        self.keyboard.press("w")
        time.sleep(duration)
        self.keyboard.release("w")
        self.keyboard.release(pynput.keyboard.Key.shift)

    def turn(self, degree):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(500 * degree), int(0))

    def back_home(self):
        print("back_home")
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(1000 * 60), int(0))
        self.keyboard.press(pynput.keyboard.Key.shift)
        self.keyboard.press("w")
        time.sleep(0.8)
        self.keyboard.release("w")
        self.keyboard.release(pynput.keyboard.Key.shift)
        time.sleep(0.5)

    def refresh_angle(self):
        print("refresh angle")
        self.keyboard.press("e")
        self.keyboard.release("e")

        self.mouse.position = (tiaoxi_pos[0], tiaoxi_pos[1])

        time.sleep(4)
        self.keyboard.press(pynput.keyboard.Key.enter)
        time.sleep(0.1)
        self.keyboard.release(pynput.keyboard.Key.enter)
        time.sleep(3)

        self.keyboard.press(pynput.keyboard.Key.esc)
        time.sleep(0.1)
        self.keyboard.release(pynput.keyboard.Key.esc)
        time.sleep(1.3)

    def run(self):
        self.refresh_angle()
        self.turn(-10)
        time.sleep(0.2)
        self.keyboard.tap("1")
        time.sleep(0.5)
        self.mouse.click(pynput.mouse.Button.middle)
        time.sleep(0.2)
        self.turn(-7)
        time.sleep(0.2)
        self.forward(3.5)
        self.turn(50)
        self.forward(1)
        self.keyboard.tap("f")
        time.sleep(2)
        self.turn(80)
        time.sleep(0.1)
        self.forward(5)
        time.sleep(0.2)
        self.turn(-70)
        time.sleep(0.2)
        self.forward(0.7)
        time.sleep(0.2)


if __name__ == "__main__":
    time.sleep(2)
    exe = ExecuteCommands()
    while True:
        exe.run()
        # break
