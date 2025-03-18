import pyautogui
import time

# Nome do usuário
pyautogui.click(190,395, duration = 1)
pyautogui.write('Teste Usuário AC')

# Telefone
pyautogui.click(488,386, duration = 1)
pyautogui.write('11912345678')

# Rodovia
pyautogui.click(224,547, duration = 1)
pyautogui.write('sp 081')
pyautogui.hotkey('enter')

# KM
pyautogui.click(519,549, duration = 1)
pyautogui.write('1')
pyautogui.hotkey('enter')

# Metro
pyautogui.click(663,553, duration = 1)
pyautogui.write('0')
pyautogui.hotkey('enter', duration = 5)
time.sleep(2)
pyautogui.hotkey('esc')

# Sentido
pyautogui.click(629,631, duration = 1)
pyautogui.click(635,743, duration = 1)

# Ocorrência
pyautogui.click(224,788, duration = 1)
pyautogui.click(245,907, duration = 1)

# Sub-Ocorrência
pyautogui.click(578,802, duration = 1)
pyautogui.click(594,936, duration = 1)

# Tipo de veículo
pyautogui.click(192,872, duration = 1)
pyautogui.click(171,702, duration = 1)

# Placa
pyautogui.click(340,877, duration = 1)
pyautogui.write('qwe1234')

# Marca
pyautogui.click(490,878, duration= 1)
pyautogui.click(493,703, duration = 1)

# Modelo
pyautogui.click(653,869, duration = 1)
pyautogui.click(664,701, duration = 1)

# Cor
pyautogui.click(174,950, duration = 1)
pyautogui.click(204,793, duration = 1)

# Ano
pyautogui.click(350,957, duration = 1)
pyautogui.write('2025')

# BTN Adicionar
pyautogui.click(493,964, duration = 1)

#scroll
pyautogui.scroll(-500)

# Observação
pyautogui.click(224,857, duration = 1)
pyautogui.write('Teste de Observação C2C')

# Salvar
pyautogui.click(321,958, duration = 1)
pyautogui.click(903,615, duration = 1)
time.sleep(5)
pyautogui.click(949,689, duration = 1)