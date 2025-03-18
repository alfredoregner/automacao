import pyautogui
import time
import datetime

# btn Adicionar
pyautogui.click(182,472, duration = 1)
time.sleep(1)

# Faixa
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# Sentido
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

campos = 0
while campos <= 1 :
# Data Interdição, Data Liberação
    data = datetime.datetime.now()
    pyautogui.press('tab')
    pyautogui.write(f'{data.strftime("%d")}', interval = 0.1)
    pyautogui.write(f'{data.strftime("%m")}', interval = 0.1)
    pyautogui.write(f'{data.strftime("%Y")}', interval = 0.1)
    pyautogui.press('tab')
    pyautogui.write(f'{data.strftime("%H")}', interval = 0.1)
    pyautogui.write(f'{data.strftime("%M")}', interval = 0.1) 
    pyautogui.press('tab')
    campos += 1

# btn Salvar
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.click(905,597, duration = 1)
time.sleep(2)
pyautogui.click(960,665, duration = 1)