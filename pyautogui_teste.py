# Programa:
import time
import pyautogui
pyautogui.PAUSE = 0.5   # esse comando atribui esse tempo de espera para cada comando pyautogui
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

x, y = 1170, 500  # Substitua pelas coordenadas 
pyautogui.moveTo(x, y, duration=8)  # Mova para as coordenadas em 1 segundo
time.sleep(0.5)  # Atraso adicional antes de clicar apenas nos locais onde eu utilizei
pyautogui.click(x, y)

pyautogui.write("https://estacio.br/")
pyautogui.press('enter')
time.sleep(1)

#x=976, y=602
pyautogui.click(976,602)
pyautogui.hotkey('ctrl','a')
pyautogui.write('ciencia da computacao')

#---------------Algumas anotações--------------------------------------
# https://pyautogui.readthedocs.io/en/latest/  ---> documentação
# pip install pyautogui
# import pyautogui
# biblioteca responsável por automatizar o mouse, o teclado e a tela do computador.
# To update, run: C:\Users\rsbez\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
# OBS: não pode colocar o nome da biblioteca como o mesmo nome do arquivo, ele não vai rodar porque haverá conflito AttributeError: partially initialized module 'pyautogui' has no attribute 'press' (most likely due to a circular import. Esse erro se resolve renomeando o arquivo.
#-----------------------------------------------------------------------
# comandos utilizados:
# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar uma tecla
# pyautogui.hotkey - combinação de teclas
# pyautogui.scroll - rolar a tela para cima ou para baixo
#------------------------------------------------------------------------
# Para usar pyautogui.click - clicar com o mouse:
#Escala de Exibição:
#Certifique-se de que as configurações de escala e layout no Windows (como o aumento de texto, aplicativos e outros itens) não estejam afetando as coordenadas. Essas configurações podem ser encontradas em Configurações > Sistema > Tela > Escala e Layout.
# NÃO ESQUEÇA: ajuste a posição de Y (altura), pois o máximo deve ser 1080.
#Para achar as coordenadas de um ícone na área de trabalho:
#import pyautogui
#import time
#print("Posicione o cursor do mouse sobre o ícone e pressione Ctrl+C para obter as coordenadas.")
#try:
#   while True:
#      x, y = pyautogui.position()
#     print(f'Coordenadas: X={x}, Y={y}', end='\r')
#        time.sleep(0.1)
#except KeyboardInterrupt:
#    print(f"\nCoordenadas finais: X={x}, Y={y}")
#    print("\nPrograma interrompido.")
#
#   ou vc pode usar o arquivo auxiliar.py que fiz com position
#
#-------------------------------------------------------------------------