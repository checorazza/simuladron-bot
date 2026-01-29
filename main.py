import pyautogui
import time
from pyautogui import ImageNotFoundException

pyautogui.FAILSAFE = True

TARGET_IMAGES = [
    "compra.png",
    "ensobrar_periodista.png"
]

LOOP_DELAY = 0.1
MOVE_DURATION = 0.1

print("Funco")

while True:
    try:
        for image in TARGET_IMAGES:
            try:
                location = pyautogui.locateOnScreen(image)

                print(f"Encontré {image}")
                x, y = pyautogui.center(location)
                pyautogui.moveTo(x, y, duration=MOVE_DURATION)
                pyautogui.click()
                break 

            except ImageNotFoundException:
                pass

        time.sleep(LOOP_DELAY)

    except KeyboardInterrupt:
        print("Bot detenido")
        break
