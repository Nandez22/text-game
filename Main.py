import pygame, sys, Menus, os, elements, webbrowser
from pygame.locals import *

#All this does is start pygame and pygame.mixer (which atm is unused as audio is complex and I am many days behind)
pygame.init()
pygame.mixer.init() 

#Hello and welcome to our project, I hope youve seen the readme (README.md) and the instructions (somewhere).
#As stated in the read me this is a menu system with a small game attached, depending at the point you downloaded this the game could be either a red box and some empty platforms or pretty flushed out...
    #With that said, the game is directly (basically 1 to 1 with some liberal interpretation to make sizing work) taken from a youtube tutorial by Clear Code (https://www.youtube.com/watch?v=YWN8GcmJ-jA)
        #-- The menus on the other hand are fully origional, while the buttons may look like the ones found on ClearCodes channel, they are redone from the ground up to work with the menu system
        #-- For the drop downs and sliders, there were no tutorials for them so those were completly origional from scratch.
            #-- I used some inspiration for the text fields but I did look up a decent chunk of the logic surrounding 'event.unicode'
    # I digress the menu fulfills the reqs of the project and are origional so while the game is from a tut it is purly there for concept and I understand if you wish to ignore it when it comes to grading
        #-- The game files are (level.py, player.py, settings.py and sprites.py)
        
#This is probably where I should mention my commenting format... I use a vsCode extension that allows me to change the format of comments called 'Better Comments' (by Aaron Bond), Name: Better Comments (https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
#Anyways, the scheme goes as follows

#  =  Dark Green -- Used to lable things and explain how they work (put down while coding for the most part)
#* = Light Green -- Comments from a 2nd pass or additional thoughts I have
#? = Cobalt Blue -- Will prolly use this for random comments about my sanity that have no bearing on the code itself (some do slip through the cracks)
#! = Bright Red  -- SOmething that needs Attention, either a warning or something to catch my eye while scrolling
#TODO = Orange   -- To Do list item, I delete these as I do things so the ammount sitting around is constantly changing

#* There is a good chance I don't fully stick to this commenting scheme as a fair warning
#! I should also note that I haven't tested this on mac for quit a few versions so there is a good chance (especiall concerning display settings) that it doesn't work at all or as intended.*

#Main looks really sad this empty :(
    #* Starts the debochery
Menus.mainMenu()

#TODO Profiles
#TODO Json For Profiles
#TODO DropDown Fix
#TODO Finish Tut for game