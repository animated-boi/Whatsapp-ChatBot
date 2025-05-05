import pyautogui
import time
import pyperclip
import openai_client

def check_last_message(copied_chat):
    message = copied_chat.strip().split(']')[-1]
    if "AnimatedBoi😉" in message:
        return False
    return True

pyautogui.click(1053, 865)
time.sleep(1)

while True:

    pyautogui.moveTo(451, 83)
    pyautogui.dragTo(1350,765, duration=1, button='left')
    pyautogui.hotkey('command', 'c')
    pyautogui.click(536, 728)
    time.sleep(1)

    copied_chat = pyperclip.paste()
    # print(copied_chat)

    if not check_last_message(copied_chat):
        print("Last message is from AnimatedBoi😉. Skipping...")
        time.sleep(1)
        continue
    response = openai_client.ai_processing(copied_chat)
    # print(response)
    pyperclip.copy(response)

    pyautogui.click(531, 789)
    time.sleep(1)

    pyautogui.hotkey('command', 'v')
    time.sleep(1)
    pyautogui.press('enter')


