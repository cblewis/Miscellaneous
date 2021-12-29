import time
from pynput.keyboard import Key, Controller

#Masterfully crafted by Cameron Lewis

keyboard = Controller()

#Paste the cheat in the '' in the cheatCode
#Run this script from command prompt, then click back into Majesty
#the script should then run and enter the cheat every 5 seconds
cheatCode = (r'prepare to die')
availableCodes = ['goblin rush',
                'give me action',
                'fill this bag',
                'prepare to die',
                'pump up the volume',
                'restoration',
                'night of the living dead']

time.sleep(3)
keyboard.press(Key.enter)
keyboard.type(cheatCode)
keyboard.press(Key.enter)

for x in range(0, 20):
    time.sleep(5)
    keyboard.press(Key.enter)
    keyboard.type(cheatCode)
    keyboard.press(Key.enter)
