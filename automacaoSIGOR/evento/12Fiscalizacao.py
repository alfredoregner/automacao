import pyautogui
import time

# toggle sem identificação
pyautogui.click(135,476, duration = 1)
time.sleep(1)

# Nome Responsável
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste Nome Responsavel', interval = 0.1)

# Telefone Responsável
pyautogui.press('tab', interval = 0.1)
pyautogui.write('11912345678', interval = 0.1)

# Embargo
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# Reincidência
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# Prodivência
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste Providencia', interval = 0.1)

# Descrição
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste Descricao', interval = 0.1)

# Motivação
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
# pyautogui.press('enter', interval = 0.1)
# pyautogui.press('down', interval = 0.1)
# pyautogui.press('enter', interval = 0.1)

# btn Adicionar
pyautogui.press('tab', interval = 0.1)
# pyautogui.press('enter', interval = 0.1)

# btn Salvar
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.click(893,599, duration = 1)
time.sleep(2)
pyautogui.click(960,674, duration = 1)
time.sleep(2)