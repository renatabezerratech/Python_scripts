from pygame import mixer

# Inicializa o mixer
mixer.init()

# Lista com os arquivos de música
playlist = ['music/all-by-myself.mp3', 'music/jungle.mp3', 'music/titanium.mp3']  # Adicione mais músicas aqui

# Função para tocar a playlist
def play_playlist(playlist):
    for music in playlist:
        mixer.music.load(music)
        mixer.music.play()

        # Espera até que a música termine ou o usuário pressione ENTER
        while mixer.music.get_busy():
            x = input(f'Tocando {music}... Digite ENTER para pular para a próxima música ou espere até terminar: ')
            if x == '':   # o Enter faz esse espaço vazio
                mixer.music.stop()
                break

# Toca a playlist
play_playlist(playlist)

print("Playlist finalizada.")
