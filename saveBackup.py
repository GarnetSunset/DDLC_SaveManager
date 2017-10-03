from distutils import dir_util
from six.moves.urllib.request import urlretrieve
import os
import sys

firstTime = 0
owd = os.getcwd()

if os.name == 'nt':
    appdata = os.getenv('APPDATA')
    ddlcDir = appdata + "/renpy/DDLC-1454445547/"
    if not os.path.isdir(appdata + "/renpy/DDLC-1454445547-backup/"):
        os.mkdir(appdata + "/renpy/DDLC-1454445547-backup/")
        copyDir = appdata + "/renpy/DDLC-1454445547-backup/"
        mkDir = appdata + "/renpy/"
        firstTime = 1
else:
    ddlcDir = "~/.renpy/DDLC-1454445547/"
    if not os.path.isdir("~/.renpy/DDLC-1454445547-backup/"):
        os.mkdir("~/.renpy/DDLC-1454445547-backup/")
        copyDir = "~/.renpy/DDLC-1454445547-backup/"
        mkDir = "~/.renpy/"
        firstTime = 1

if firstTime == 1:
    print("Since this is your first time, I'll run this backup for you.\n")
    dir_util.copy_tree(ddlcDir, copyDir)
    
while(input != 0):
    input = raw_input("What do you wanna do?\n1. Backup your saves again (This will overwrite your old ones)\n2. Delete the persistent file (allows you to restart the game and stuff with your saves, this will also add the .chr's back)\n3. Wipe my saves (will add chr's back to the character dir)\n4. Restore the Saves\n0. Exit\n>")    
    if(input == "0"):
        print("Bye!")
        sys.exit()
        
    if(input == "1"):
        dir_util.copy_tree(ddlcDir, copyDir)
        print("Copied and Overwritten!\n")
        
    if(input == "2"):
        try:
            os.remove(ddlcDir + "persistent")
        except:
            print("Already removed!\n")
        if not os.path.exists(owd + "/characters/monika.chr"):
            urlretrieve("https://i.imgur.com/3c1qJaA.jpg","characters/monika.chr")
        if not os.path.exists(owd + "/characters/yuri.chr"):
            urlretrieve("https://i.imgur.com/3c1qJaA.jpg","characters/yuri.chr")
        if not os.path.exists(owd + "/characters/sayori.chr"):
            urlretrieve("https://i.imgur.com/3c1qJaA.jpg","characters/sayori.chr")
        if not os.path.exists(owd + "/characters/natsuki.chr"):
            urlretrieve("https://i.imgur.com/3c1qJaA.jpg","characters/natsuki.chr")
        print("Removed the persistent file and added the girls back!\n")
        
    if(input == "3"):
        dir_util.remove_tree(ddlcDir)
        os.mkdir(mkDir + "DDLC-1454445547/")
        if not os.path.exists(owd + "/characters/monika.chr"):
            urlretrieve("https://i.imgur.com/3c1qJaA.jpg","characters/monika.chr")
        if not os.path.exists(owd + "/characters/yuri.chr"):
            urlretrieve("https://i.imgur.com/3c1qJaA.jpg","characters/yuri.chr")
        if not os.path.exists(owd + "/characters/sayori.chr"):
            urlretrieve("https://i.imgur.com/3c1qJaA.jpg","characters/sayori.chr")
        if not os.path.exists(owd + "/characters/natsuki.chr"):
            urlretrieve("https://i.imgur.com/3c1qJaA.jpg","characters/natsuki.chr")
        print("Deleted all Saves and added the girls back!\n")
        
    if(input == "4"):
        dir_util.copy_tree(copyDir, ddlcDir)
        print("Restored and Overwritten!\n")
    print("What next?\n")
