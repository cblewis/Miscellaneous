
#Masterfully crafted by Cameron Lewis

with open ("MP3 bitrate.txt", 'r', encoding='utf-8') as bitratefile:
    with open ('MP3 bitrate - songs to replace.txt', 'w', encoding='utf-8') as outputfile:
    lines = bitratefile.readlines()
    bitrates = [line.split('\n') for line in lines]
        for bitrate in bitrates:
           data = bitrate[0].split(',')
            #the [0] entry for bitrate is the str version of the list including song and bitrate
           if data[1][1].isdigit():
               # data[1][0] seems to be empty
               if data[1][1] != '3':
                   #this is a str, and is problematic trying to convert to
                   #int or to float
                   outputfile.write(str(bitrate) + '\n')
