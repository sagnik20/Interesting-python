from pygame import mixer

mixer.init()
mixer.music.load(music.mp3)
mixer.music.set_volume(0.6)
mixer.music.play()

while True:
    print("Press : \n 'p' to pause \n 'r' to resume \n 's' to stop \n 'f' to stop while fading out \n 'w' to rewind \n")
    print("\n Press 'e' to exit the music player \n: ")
    query = input()

    if(query == 'p'):
        mixer.music.pause()
        #pause the music
    elif(query == 'r'):
        mixer.music.unpause()
        #resume the music
    elif(query == 's'):
        mixer.music.stop()
        #stops the music doesn't unload it
    elif(query == 'f'):
        mixer.music.fadeout()
        #stops after fading out
    elif(query == 'w'):
        mixer.music.rewind()
        #restart music
    elif(query == 'e'):
        mixer.music.stop()
        mixer.music.unload()
        break
    else:
        print("Worng Input")
        continue
