# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with several.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
#while cave != '1' and cave != '2':
#Indent had to be deleted 
  
    while cave != '1' and cave != '2':
            print('Which cave will you go into? (1 or 2)')
            cave = input()
#return caves
#Delete the s in caves. Try this :  return cave
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
#print 'Gobbles you down in one bite!'
#No parentheses around the text that wanted to be printed.Try this instead : print ('Gobbles you down in one bite!')
        print ('Gobbles you down in one bite!')


displayIntro()
#caveNumber = choosecave()
#Capitalize the C in Cave. Try this : caveNumber = chooseCave()
caveNumber = chooseCave()
checkCave(caveNumber)
    
#print("Thanks for planing")
#I think you were trying to spell "playing" instead of "planing". Try this: print("Thanks for playing")
print("Thanks for playing")
