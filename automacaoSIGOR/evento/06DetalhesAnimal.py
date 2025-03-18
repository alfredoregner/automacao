import pyautogui
import time

# btn Adicionar
pyautogui.click(182,472, duration = 1)
time.sleep(1)

# Provável Responsável
pyautogui.click(540,275, duration = 1)
time.sleep(1)

# btn Adicionar Provável Responsável
pyautogui.click(740,236, duration = 1)
time.sleep(1)

# Nome
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste de Nome', interval = 0.1)

# Telefone
pyautogui.press('tab', interval = 0.1)
pyautogui.write('11912345678', interval = 0.1)

# Celular
pyautogui.press('tab', interval = 0.1)
pyautogui.write('11987654321', interval = 0.1)

#btn Salvar
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# btn Confirmar Provável Responsável
pyautogui.click(897,605, duration = 1)
time.sleep(1)
pyautogui.press('enter', interval = 0.1)
time.sleep(1)

# Animal
pyautogui.click(543,231, duration = 1)
time.sleep(1)

# Localização X
pyautogui.press('tab', interval = 0.1)
pyautogui.write('123456', interval = 0.1)

# Localização Y
pyautogui.press('tab', interval = 0.1)
pyautogui.write('987654', interval = 0.1)

# Fuso, Nome Polular, Condição do Animal, Porte do Animal
comboboxFNCP = 0
while comboboxFNCP <= 3:
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('enter', interval = 0.1)
    pyautogui.press('down', interval = 0.1)
    pyautogui.press('enter', interval = 0.1)
    comboboxFNCP += 1

# Sinais Particulares
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste de Sinais Particulares', interval = 0.1)

    # Condições do Entorno, Providência Primária, Providência Secundária, Destinação
comboboxCPPD = 0
while comboboxCPPD <= 3:
    pyautogui.press('tab', interval = 0.1)
    pyautogui.press('enter', interval = 0.1)
    pyautogui.press('down', interval = 0.1)
    pyautogui.press('enter', interval = 0.1)
    comboboxCPPD += 1

# Removido Por
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste Removido Por', interval = 0.1)

# Provável Responsável
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# Observações
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste de Observacoes', interval = 0.1)

# btn Salvar
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.click(905,597, duration = 1)
time.sleep(2)
pyautogui.click(960,665, duration = 1)