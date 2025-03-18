import pyautogui
import time
import datetime

# btn Adicionar
pyautogui.click(182,472, duration = 1)
time.sleep(1)

# Recurso
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
time.sleep(1)

campos = 0
while campos <= 2:
# Data Acionamento, Data Início, Data Término
    pyautogui.press('tab')
    data = datetime.datetime.now()
    pyautogui.write(f'{data.strftime("%d")}', interval = 0.1)
    pyautogui.write(f'{data.strftime("%m")}', interval = 0.1)
    pyautogui.write(f'{data.strftime("%Y")}', interval = 0.1)
    pyautogui.write(f'{data.strftime("%H")}', interval = 0.1)
    pyautogui.write(f'{data.strftime("%M")}', interval = 0.1) 
    time.sleep(0.5)     
    campos += 1    

# Odômetro Inicial
pyautogui.press('tab', interval = 0.1)
pyautogui.write('1500', interval = 0.1)
time.sleep(0.5)

# Odômetro Final
pyautogui.press('tab', interval = 0.1)
pyautogui.write('2000', interval = 0.1)
time.sleep(0.5)

# Salvar
pyautogui.press('tab', interval = 0.1) # Recursos Externos
pyautogui.press('tab', interval = 0.1) # btn Fechar
pyautogui.press('tab', interval = 0.1) # btn Salvar
pyautogui.press('enter', interval = 0.1)
pyautogui.click(905,597, duration = 1)
time.sleep(2)
pyautogui.press('enter')