import pyautogui
import time

# Patrimônio
pyautogui.click(182,472, duration = 1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
time.sleep(0.5)       

# Quantidade
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.write('10', interval = 0.1)
time.sleep(0.5) 

# Observação
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste Observacao Danos ao Patrimonio')
time.sleep(0.5) 

# btn Salvar
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.click(905,597, duration = 1)
time.sleep(2)
pyautogui.click(960,665, duration = 1)