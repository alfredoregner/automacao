import pyautogui
import time

# Descrição
pyautogui.click(318,469, duration = 1)
time.sleep(2)

# Checkbox dos tipos de acidente
pyautogui.click(561,469, duration = 1) # Colisão Traseira
pyautogui.click(560,488, duration = 1) # Capotamento
pyautogui.click(560,518, duration = 1) # Colisão Transversão
pyautogui.click(872,467, duration = 1) # Colisão Frontal
pyautogui.click(871,494, duration = 1) # Atropelamento de Pedestre
pyautogui.click(871,522, duration = 1) # Atropelamento de Animal
pyautogui.click(1172,465, duration = 1) # Colisão Lateral
pyautogui.click(1174,497, duration = 1) # Outros
pyautogui.click(1174,526, duration = 1) # Tombamento
pyautogui.click(1486,465, duration = 1) # Choque
pyautogui.click(1481,496, duration = 1) # Engavetamento
pyautogui.click(1482,519, duration = 1) # Queda

# Descrição do Acidente
pyautogui.click(580,598, duration = 1)
pyautogui.write('Teste de descrição do Acidente', interval = 0.1)

# Token
pyautogui.press('tab', interval = 0.1)
pyautogui.write('12345', interval = 0.1)

#Causa Provável
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# Salvar
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
time.sleep(2)
pyautogui.click(903,598, duration = 1)
time.sleep(2)
pyautogui.press('enter', interval = 0)

# Vítimas
pyautogui.click(335,515, duration = 1)
time.sleep(2)

# btn Adicionar
pyautogui.click(597,473, duration = 1)
time.sleep(2)

# Tipo de Vítima
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# Nome
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste Nome Condutor', interval = 0.1)

# Gravidade
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# Veículo
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# Removido Por
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# Removido Para
pyautogui.press('tab', interval = 0.1)
pyautogui.write('Teste Removido Para', interval = 0.1)

# Tipo de Cinto
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# Usava Cinto?
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.press('down', interval = 0.1)
pyautogui.press('enter', interval = 0.1)

# btn Salvar
pyautogui.press('tab', interval = 0.1)
pyautogui.press('tab', interval = 0.1)
pyautogui.press('enter', interval = 0.1)
pyautogui.click(899,603, duration = 1)
time.sleep(2)
pyautogui.click(970,670, duration = 1)
