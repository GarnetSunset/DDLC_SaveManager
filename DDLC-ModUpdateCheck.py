from six.moves.urllib.request import urlopen
import os
import webbrowser

if not os.path.exists("game/lastVer"):
    resp = urlopen('http://tiny.cc/ddlcmod')
    resp.getcode()
    url = open("game/lastver", "w")
    url.write(resp.url)
    url.close()
    
resp = urlopen('http://bit.ly/bcFOko')
resp.getcode()

with open('game/lastVer', 'r') as verNum:
    data=verNum.read()

if(resp.url != data):
    webbrowser.open('http://tiny.cc/ddlcmod', new=0, autoraise=True)
    print("Please update!!!")
