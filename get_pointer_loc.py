c

while True:
    x, y = pyautogui.position()

    print(f"Mouse position: ({x}, {y})")
    pyautogui.sleep(0.5)