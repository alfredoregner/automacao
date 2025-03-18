import pyautogui
import time

add = 0
while add <= 3:
# Escolher Arquivo
    pyautogui.click(182,472, duration = 1)
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('enter', interval = 0.1)
    time.sleep(2)
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('down', interval = 0.1)
    pyautogui.press('enter', interval = 0.1)
    
    # Enviar Imagem
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('enter', interval = 0.1)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    add += 1