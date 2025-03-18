import pyautogui
import time

# Clique na tela para garantir que está na página
pyautogui.click(182,472, duration = 1)
time.sleep(1)

# Quantidade
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.write('10', interval = 0.1)

# Providência
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste Providencia', interval = 0.1)

# Descrição
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste Descricao', interval = 0.1)

# Causa / Motivo
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# btn Adicionar
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)


# Tipo / Espécie
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# btn Adicionar
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)


# Consequências
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# btn Adicionar
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)


# Requisição Operacional
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# btn Adicionar
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# btn Salvar
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.click(893,599, duration = 1)
time.sleep(2)
pyautogui.click(960,674, duration = 1)
time.sleep(2)