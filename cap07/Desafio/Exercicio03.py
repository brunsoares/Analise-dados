import pyautogui
import time

print("Movendo mouse para canto superior esquerdo")
print(f"Posição atual do mouse: {pyautogui.position()}")
pyautogui.moveTo(0, 0, duration=3)
pyautogui.FAILSAFE = False  # Ao colocar no canto esquerdo superior ocorre o FailSafe
time.sleep(2)

print("Movendo mouse para canto inferior esquerdo")
print(f"Posição atual do mouse: {pyautogui.position()}")
pyautogui.moveTo(1, 760, duration=3)
time.sleep(2)

print("Movendo mouse para canto inferior direito")
print(f"Posição atual do mouse: {pyautogui.position()}")
pyautogui.moveTo(1360, 760, duration=3)
time.sleep(2)

print("Movendo mouse para canto superior direito")
print(f"Posição atual do mouse: {pyautogui.position()}")
pyautogui.moveTo(1360, 0, duration=3)
time.sleep(2)

print("Movendo mouse para canto superior esquerdo")
print(f"Posição atual do mouse: {pyautogui.position()}")
pyautogui.moveTo(0, 0, duration=3)
time.sleep(2)

