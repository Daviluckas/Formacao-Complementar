from pygame import mixer
mixer.init()
musica = mixer.music.load('ex021.mp3')
mixer.music.play()
Parar = input('Digite algo para parar:')
