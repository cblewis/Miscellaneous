from mutagen.mp3 import MP3
import os

#Masterfully crafted by Cameron Lewis

filepath = "C:/Users/Slim Low/Music/"
with open ('MP3 bitrate.txt', 'w', encoding='utf-8') as outputfile:
    outputfile.write("MP3 Filename, Bitrate" + "\n")
    try:
        for dirpath, dirnames, filenames in os.walk(filepath):
            for file in filenames:
                if file.endswith(".mp3"):
                    mp3path = (filepath + file)
                    mp3file = MP3(mp3path)
                    #print(file, mp3file.info.bitrate / 1000)
                    outputfile.write(file + ', ' + str(mp3file.info.bitrate / 1000) + '\n')
    except AssertionError as error:
        print(error)
