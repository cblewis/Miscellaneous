import random, time

class adventurer:
    def __init__ (self, name, swordsmanship, experience, wit, stamina, armament):
        self.name = name
        self.swordsmanship = swordsmanship
        self.experience = experience
        self.wit = wit
        self.stamina = stamina
        self.armament = armament

Namae = ['Roland', 'Jasper', 'Roger', 'Richard', 'Louis', 'Robert', 'Harald']
SwordSkill = ['master', 'adept', 'good', 'poor']
Exp = ['master', 'adept', 'good', 'poor']
Nouryouku = ['witty', 'quick-thinking', 'able-minded', 'slow-thinking']
Tairyouku = ['tireless', 'healthy', 'low', 'poor']

#castle names
Castle = ["Meade", "Feathergale", "Harlick", "Warwick", "Bastille", "Exeter", "Lancaster", "York"]

#creates an armory into which the inputted weapons are stored
Armory = []
FirstWep = input("Please type the name of a weapon that you wish an adventurer to wield: ")
SecondWep = input("Please type the name of another weapon that you wish an adventurer to wield: ")
ThirdWep = input("Please type one more name of a weapon that you wish an adventurer to wield: ")
Armory.append(FirstWep)
Armory.append(SecondWep)
Armory.append(ThirdWep)

#randomly chooses a weapon for each adventurer. past choice was to input a weapon individually for each adventurer.
Adv1Weapon = random.choice(Armory) #input("Give this man a weapon: ")
Adv2Weapon = random.choice(Armory) #input("Give this man a weapon: ")
Adv3Weapon = random.choice(Armory) #input("Give this man a weapon: ")

#list of adventurers. Objects from the adventurer class.
adventurer1 = adventurer(random.choice(Namae), random.choice(SwordSkill), random.choice(Exp), random.choice(Nouryouku), random.choice(Tairyouku), Adv1Weapon)
adventurer2 = adventurer(random.choice(Namae), random.choice(SwordSkill), random.choice(Exp), random.choice(Nouryouku), random.choice(Tairyouku), Adv2Weapon)
adventurer3 = adventurer(random.choice(Namae), random.choice(SwordSkill), random.choice(Exp), random.choice(Nouryouku), random.choice(Tairyouku), Adv3Weapon)

TestM = {adventurer1, adventurer2, adventurer3}
Mononofu = [adventurer1.name, adventurer2.name, adventurer3.name]

print(adventurer1.name + " is summoned to your presence. He is a " + adventurer1.wit + " man. You give him a " + adventurer1.armament + " on account of him being a " + adventurer1.swordsmanship + " warrior.")
time.sleep(4)
print(adventurer2.name + " receives a " + adventurer2.armament + " on account of his " + adventurer2.swordsmanship + " prowess.")
time.sleep(4)
print(adventurer3.name + " comes prepared with a " + adventurer3.armament + " because he is a " + adventurer3.wit + " individual.")
time.sleep(3)

#selecting adventurers at random from a dictionary
randomwarriors =[adventurer1, adventurer2, adventurer3]
assert isinstance(randomwarriors, object)
randomwarrior = random.choice(randomwarriors)

print(str(Mononofu) + " all depart for " + random.choice(Castle) + " castle. " + randomwarrior.name + " arrives first on account of his " + randomwarrior.stamina + " energy, weilding his " + randomwarrior.armament)

Diceroll = [1,2,3,4,5,6,7,8,9,10,11,12]
Roll = random.sample(range(Diceroll))
if Roll >= 7:
    print("The adventurers were successful in storming the castle .")
else:
    print("The adventurers were not successful and are beaten back.")

while Roll >= 8:
    print("The adventurers next head toward " + random.choice(Castle) + ("."))
    if Roll >= 7:
        print("The adventurers were successful in storming the castle .")
    else:
        print("The adventurers were not successful and are beaten back.")
