print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
import random
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
Waypoint1 = input('You have entered the labyrinth and have ended up at a crossroad. You can go "left" or "right". Please type your answer:\n').lower()

if Waypoint1 == "left":
    Waypoint2 = input('After several uneventful minutes you have reached the lake in the middle of the labyrinth.'
                      'There is a ferryman in the distance do you "wait" for the ferry or will you take your chances and attempt to "swim"? \n'
                      'Please type your answer: \n').lower()
    if Waypoint2 == "wait":
        Waypoint3 = input('You wait for they ferry and are ferried through a small inlet not visible from the shore you were just on. \n'
                          'In the clearing you see an island with 3 free-standing doors of different of different colours; "red", "blue", and "yellow".\n'
                          'Which colour of door would you like to enter? Please type your answer: \n').lower()
        if Waypoint3 == "yellow":
            print('You try to push open the "yellow" door to no avail....\n'
                  'you contemplate changing your choice but your stubbornness prevails and you struggle on.\n'
                  'After a few more minutes pushing the door you give up and pull the door in frustration. \n'
                  'The door flies open and you fall back not expecting the door to open. The metalic sound of gold falling onto the floor tingles your ear.\n'
                  'You have found the treasure! Winner!')
            input("<Press enter to exit>")
        elif Waypoint3 == "red":
            print('As you place your hand on the door the other doors fade away. '
                  'The door suddenly bursts into black flames scorching your hand and setting it alight.\n'
                  'In a panic you run back to the water but to no avail as hellfire will continue to burn until you are nothing but dust and ash. '
                  '\nGame Over.')
        elif Waypoint3 == "blue":
            print('You place your hand on the "blue" door and the other doors fade away. The door is cold...'
                  'after a couple of seconds there is a flash and you are frozen solid. '
                  'As everything fades to black you hear a mocking voice laughing at your demise.\n'
                  'Game Over.')
        else:
            if random.randint(0,10) <= 5 :
                print("Nothing happens and all doors fade away revealing the ferryman as they lunge at you striking you swiftly in the neck."
                      " You fall to your knees and gasp for breath. \n"
                      "The ferryman looms over you for a second. With a smirk, they crouch down and whispers into your ear.\n"
                      "\"Game Over.\"")
            else:
                print('You blank out for a second and remember you left the stove on back at home and you wander back.')

    if Waypoint2 == "swim":
        if random.randint(0,10) <= 5:
            print('You have chosen to take your chances with the water. You remember something from your first-aid training...something about hypothermia...'
                  ' but can\'t quite recall.\n'
                  'Not taking any chances you throw on all of the clothes you have and descend into the water.\n'
                  'After a couple of minutes you remember that air is a thing and you have just been drinking water the whole time. \n'
                  'In a panic you thrash around frantically to no avail as all the clothing is weighing you down.\n'
                  'The world fades to black. Game Over.')
        else:
            print('Something in the back of your mind is telling you to not go into the water.\n'
                  'That has never stopped you before. You dive right into the water. Unbeknown to you there is no oxygen in this water and you sink.\n'
                  'Slowly at first but gradually gaining speed. The light around you fades away and you are left in darkness.\n'
                  'Your feet hit the bottom and you sink further as if you are being swallowed by the ground.\n'
                  'Your head goes under and you are pushed out into a chair in a white room. You can breath, there is air here.\n'
                  'There is a flash and you realized you have been isekai-ed and are now a newborn baby.\n'
                  'Try Again.')
    else:
        print('You decide this is not worth your time and turn back the way you came. Honestly you don\'t remember why you came in the first place.'
              'You rack your brain and conclude that it probably wasn\'t that important anyway and head home.\n'
              'It\'ll come to you eventually.\nTry Again.')

elif Waypoint1 == "right":
    if random.randint(0,10) <= 5:
        print('Deciding going right is the best course of action you break into a full sprint. You have always been confident in your speed.\n'
              'But your impatience was your undoing. Since on the right is a very steep and slippery hill. '
              'The momentum carries you all the way down the hill.\n'
              'You have reached Mach 5, 5 times the speed of sound. At the bottom of the hill you slam into a wall.\n'
              'Game Over.')
    else:
        print('You walk down the path to the right and slowly descend down a hill. Being careful not to slip you make it down to the bottom.\n'
              'There is a wall dangerously close to the bottom of the hill. '
              'You notice a dark spot on the wall and several indentations roughly human sized.\n'
              'You continue to wander aimlessly your cautious nature proving useful as you narrowly escape death many times.\n'
              'Unable to find your way through this labyrinth you decide to at least make yourself comfortable.\n'
              'You live a long but difficult life in the labyrinth but ultimately are unable to leave.\n'
              'Try Again.')
else:
    if "smash" in Waypoint1 :
        print("You decide that neither way is where you want to go and decide to go right through the wall in front of you.")
        if random.randint(1,2) == 2 :
            print('With a surge of power you plow through the wall in front of you and find yourself in a room of enormous wealth.\n'
                  'You look around in awe, slowly taking everything in. But the hole you just made quickly closes up behind you leaving you stranded. \n'
                  'You have found the riches of the labyrinth but have no way out. You sit there...with nothing else to do you start counting your riches.\n'
                  'Try Again.')
        else:
            print('With nothing to lose you back up slowly to charge into the wall. For a brief moment there is a flicker of movement on the wall.\n'
                  'You run with all of your might right at the wall. A hold opens up and there is a half second where you think '
                  '"Cool. My intuition is never wrong."'
                  'Unbeknown to you the wall itself was a mimic that swallowed you whole.\n'
                  'Game Over.')
    elif random.randint(0,10) <= 5:
        print('You have seen this in the movies and decide this whole thing is a trick.'
              ' You muster your courage and charge right at the wall in front of you.\n'
              'You hear something crack and a flash of pain engulfs your body. You let out a sharp yelp as you lay on the floor clutching your head.\n'
              'As you contemplate your actions your yelp has attached some of the creatures of the labyrinth. \n'
              'You have become acutely aware of the sounds of the labyrinth. The flurry of sounds reverberate in your ears until....\n'
              'everything is silent. Everything fades to black as the creatures of the labyrinth have taken you.\n'
              'Game Over. ')
    else:
        print('Nothing happens and the labyrinth as if with a mind of it\'s own smites you where you stand.\n'
              'Game Over.')
  
