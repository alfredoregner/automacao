import pyautogui
import time

# btn Adicionar
pyautogui.click(182,472, duration = 1)
time.sleep(1)

# Condutor
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste de Condutor', interval = 0.1)

# Telefone
pyautogui.press('tab', interval = 0.1)
pyautogui.write('11912345678', interval = 0.1)

# Placa
pyautogui.press('tab', interval = 0.1)
pyautogui.write('tes1234', interval = 0.1)

combobox = 0
while combobox <= 3: 
# Marca, Modelo, Cor, Tipo de Veículo
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('enter', interval = 0.1)
    pyautogui.press('down', interval = 0.1)
    pyautogui.press('enter', interval = 0.1)
    time.sleep(1)
    combobox += 1

# Ano
pyautogui.press('tab', interval = 0.1)
pyautogui.write('2025', interval = 0.1)
pyautogui.press('tab', interval = 0.1)

removido = 0
while removido <= 1: 
# Removido Por, Removido Para
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('enter', interval = 0.1)
    pyautogui.press('down', interval = 0.1)
    pyautogui.press('enter', interval = 0.1)
    removido += 1

# Salvar
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
time.sleep(2)
pyautogui.click(960,665, duration = 1)