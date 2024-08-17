
import os
import tkinter as tk
from pygame import mixer

# Inicializa o mixer do pygame
mixer.init()

# Nome da pasta de músicas (localizada no mesmo diretório do código)
music_folder = 'music'

# Caminho completo da pasta de músicas
music_folder_path = os.path.join(os.getcwd(), music_folder)

# Lista de arquivos .mp3 na pasta
playlist = [f for f in os.listdir(music_folder_path) if f.endswith('.mp3')]
current_song_index = 0

# Função para tocar a playlist
def play_music():
    global current_song_index
    if current_song_index < len(playlist):
        music_path = os.path.join(music_folder_path, playlist[current_song_index])
        mixer.music.load(music_path)
        mixer.music.play()
        print(f"Tocando: {playlist[current_song_index]}")
    else:
        print("Fim da playlist.")
        stop_music()

# Função para pular para a próxima música
def next_music():
    global current_song_index
    if current_song_index < len(playlist) - 1:
        mixer.music.stop()
        current_song_index += 1
        play_music()
    else:
        print("Não há mais músicas na playlist.")

# Função para parar a música e encerrar o programa
def stop_music():
    mixer.music.stop()
    root.quit()

# Cria a janela principal
root = tk.Tk()
root.title("Playlist MP3")

# Botão para iniciar a playlist
play_button = tk.Button(root, text="Tocar playlist", command=play_music)
play_button.pack(pady=10)

# Botão para pular para a próxima música
next_button = tk.Button(root, text="Próxima música", command=next_music)
next_button.pack(pady=10)

# Botão para encerrar a playlist e parar o programa
stop_button = tk.Button(root, text="Encerrar", command=stop_music)
stop_button.pack(pady=10)

# Inicia o loop da interface gráfica
root.mainloop()




