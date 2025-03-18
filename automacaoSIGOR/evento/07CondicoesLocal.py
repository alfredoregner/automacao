import pyautogui
import time

# btn Adicionar
pyautogui.click(182,472, duration = 1)
time.sleep(1)

# Traçado da Pista
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
time.sleep(0.5)       

# Relevo
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
time.sleep(0.5) 

# Conservação do Pavimento
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
time.sleep(0.5) 

# Sinalização Vertical
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
time.sleep(0.5) 

# Sinalização Horizontal
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
time.sleep(0.5) 

# Superfície da Pista
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('down', interval = 0.1)                                 
pyautogui.press('down', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
time.sleep(0.5) 

# Outros
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste Outros Superficie', interval = 0.1)
time.sleep(0.5) 

# Meteorologia
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.hotkey('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
time.sleep(0.5) 

# btn Salvar
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.click(905,597, duration = 1)
time.sleep(2)
pyautogui.press('enter')