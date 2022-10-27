#!/usr/bin/env python3
import pyautogui, time

cheates = [
    "HESOYAM",
    "PROFESSIONALSKIT"
]



def s(x):
    time.sleep(x)

def u(x):
    pyautogui.keyUp(x)

def d(x):
    pyautogui.keyDown(x)

def press(keyList):
    for y in keyList:
        tlist = list(y.replace(" ", ""))
        for x in tlist:
            d(x)
            u(x)

def main():
    while True:
        press(cheates)
        # s(0.01)




if __name__ == "__main__":
    s(10)
    main()
