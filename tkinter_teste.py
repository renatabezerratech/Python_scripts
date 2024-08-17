import tkinter as tk
from tkinter import simpledialog

# Inicializa a janela principal (que pode ficar oculta)
root = tk.Tk()
root.withdraw()  # Oculta a janela principal

# Cria a caixa de diálogo de entrada
user_input = simpledialog.askstring("Entrada", "Digite algo:")

# Exibe o valor inserido pelo usuário
print("Você digitou:", user_input)
