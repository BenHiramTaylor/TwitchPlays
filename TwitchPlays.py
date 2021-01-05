# Hello!
# This file contains the main logic to process Twitch chat and convert it to game commands.
# All sections that you need to update are labeled with a "TODO" comment.
# The source code primarily comes from:
    # Wituz's "Twitch Plays" tutorial: http://www.wituz.com/make-your-own-twitch-plays-stream.html
    # PythonProgramming's "Python Plays GTA V" tutorial: https://pythonprogramming.net/direct-input-game-python-plays-gta-v/

# There are 2 other files needed to run this code:
    # TwitchPlays_AccountInfo.py is where you put your Twitch username and OAuth token. This is to keep your account details separated from the main source code.
    # TwitchPlays_Connection.py is the code that actually connects to Twitch. You should not modify this file.

# Disclaimer: 
    # This code is NOT optimized or well-organized. I am not a Python programmer.
    # I created a simple version that works quickly, and I'm sharing it for educational purposes.

###############################################
# Import and define our functions / key codes to send key commands

# General imports
import time
import pyautogui

# Twitch imports
import TwitchPlays_Connection
from TwitchPlays_AccountInfo import TWITCH_USERNAME, TWITCH_OAUTH_TOKEN

def PressAndHoldKey(Key,Seconds):
    try:
        pyautogui.keyDown(Key)
        time.sleep(Seconds)
        pyautogui.keyUp(Key)
    except:
        print(f"Couldn't hold Key: {Key} for {Seconds} seconds.")

# An optional countdown before the code actually starts running, so you have time to load up the game before messages are processed.
# TODO: Set the "countdown" variable to whatever countdown length you want.
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

# Connects to your twitch chat, using your username and OAuth token.
# TODO: make sure that your Twitch username and OAuth token are added to the "TwitchPlays_AccountInfo.py" file
t = TwitchPlays_Connection.Twitch()
t.twitch_connect(TWITCH_USERNAME, TWITCH_OAUTH_TOKEN)

while True:
    # Check for new chat messages
    new_messages = t.twitch_recieve_messages()
    if not new_messages:
        #No new messages. 
        continue
    else:
        try:  
            for message in new_messages:
                # We got a new message! Get the message and the username.
                msg = message['message'].lower()
                username = message['username'].lower()
                
                #TODO UPDATE LIST OF KEYS YOU WISH TO HAVE PRESSED
                keysToPress = ["a"]

                # PRINTS MESSAGE FOR DEBUGGING AND ENSURING ALL WORKS FINE
                print(msg)

                #TODO ADD ALL KEYS YOU WISH TO TRIGGER ON MESSAGES HERE
                if msg in keysToPress:
                    pyautogui.press(msg)

                if msg == "drive":
                    PressAndHoldKey("W",3)
        except:
            # There was some error trying to process this chat message. Simply move on to the next message.
            print('Encountered an exception while reading chat.')