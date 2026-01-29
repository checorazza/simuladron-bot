import pyautogui
import time
from pyautogui import ImageNotFoundException

pyautogui.FAILSAFE = True

TARGET_IMAGES = [
    "compra.png",
    "ensobrar_periodista.png",
    "moneda.png",
]

LOOP_DELAY = 0.1
MOVE_DURATION = 0.1

print("Funco")

while True:
    try:
        for image in TARGET_IMAGES:
            try:
                print(f"Buscando {image}...")
                location = pyautogui.locateOnScreen(image)

                print(f"Encontré {image}")
                x, y = pyautogui.center(location)
                pyautogui.moveTo(x, y)
                pyautogui.click()
                break 

            except ImageNotFoundException:
                print(f"No encontré {image}, buscando siguiente...")
                pass

        time.sleep(LOOP_DELAY)

    except KeyboardInterrupt:
        print("Bot detenido")
        break
