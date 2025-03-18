import pyautogui
from time import sleep

# Comando para abrir a captura do mouse: 
# 1. cmd
# 2. from mouseinfo import mouseInfo
# 3. mouseInfo()

# Realizar login de usuário
# Colocando usuário
pyautogui.click(936,662, duration = 1)
pyautogui.write('operadorc2c')

# Colocando senha
pyautogui.click(941,746, duration = 1)
pyautogui.write('der@123')

pyautogui.click(1028,800, duration = 1)