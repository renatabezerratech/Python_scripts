from pygame import mixer
mixer.init()
mixer.music.load('all-by-myself.mp3')
mixer.music.play()
x = input('Digite ENTER para parar...')



#Assim funcionou no VScode, mas o mp3 não finaliza:
#from pygame import mixer
#mixer.init()
#mixer.music.load('Experiencia.mp3')
#mixer.music.play()
#import time
#time.sleep(360)

#Assim não funciona no VScode:
#import pygame
#pygame.init()
#pygame.mixer.music.load('Experiencia.mp3')
#pygame.mixer.music.play() 
#pygame.event.wait()

# https://www.pygame.org/docs/
# python -m pip install -U pygame
# pip install pygame --upgrade
# teste no cmd: python -m pygame.examples.aliens 
# https://pt.stackoverflow.com/questions/288050/