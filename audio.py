
from time import sleep
import os
import RPi.GPIO as GPIO
import vlc
from twilio.rest import Client
from test import testStruct

# twilio setup
account_sid = '[REDACTED]'
twilioSender = "[REDACTED]"
#SECRET KEY!!!!!!!
auth_token = '[REDACTED]'
client = Client(account_sid, auth_token)

GPIO.setmode(GPIO.BOARD)
# sets the buttons pins
button1 = 16
button2 = 18
button3 = 22
switch = 24
# sets the buttons to read input
GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# locations for the GPS aspect of the project
# the coords go to 3 decimal places
# the format is as follows:
# [x-coord, y-coord, audio file]
locations =  [
	testStruct,
]
	
# song files for the seek  option
songs = [
	"/home/101/hackathon/coin.mp3",
	"/home/101/hackathon/celeste.m4a",
	"/home/101/hackathon/FurElise.wav",
	"/home/101/hackathon/moon.m4a",
	"/home/101/hackathon/sonata.ogg"
]
# sets the current postion in the list of songs
pos= 0
# gets the loaction of the user
# should use GPS and an api to get long/lat
def getLocation():
	#calling API to get location  via coords
	#print(GPIO.input(switch))
	if(GPIO.input(switch)==1):
		return [50.5050, 45.4545]
	else:
		return [0.000,0.000]

# selects the first song 
player = vlc.MediaPlayer(songs[pos])
# sets the starting location to 0,0
# used for testing 
currentLocation =  [0.0000,0.0000]
while(1 ==1):
	# first button: handles play/pasue
	if(GPIO.input(button1)==1):
		print("Button1 on")
		if player.is_playing():
			player.pause()
			print("paused")
		else:
			player.play()
			print("playing")
		sleep(.5)
	# seek to start next song
	elif(GPIO.input(button2)== 1):
		print("Button2 on")
		player.stop()
		pos +=1
		player = vlc.MediaPlayer(songs[pos % len(songs)])
		player.play()
		sleep(.5)
	# prev to start prevous song
	elif(GPIO.input(button3)== 1):
		print("Button3 on")
		player.stop()
		pos -=1
		player = vlc.MediaPlayer(songs[pos % len(songs)])
		player.play()
		sleep(.5)
	# checks if the song has finsihed
	# playes the next song
	if (str(player.get_state()) == "State.Ended"):
		print("next song please")
		pos += 1
		player = vlc.MediaPlayer(songs[pos % len(songs)])
		player.play()
	# gets the location
	newLocation = getLocation()
	# if the user changed locations
	# check if that location has a song attached to it
	# and play it
	# sets the newLocation to the currentLocation
	if(newLocation != currentLocation):
		for x in locations:
			if(x["coords"][0] == newLocation[0] and x["coords"][1] ==newLocation[1]):
				if(str(player.get_state()) != "State.NothingSpecial"):	
					player.stop()
				player = vlc.MediaPlayer(x["file"])
				player.play()
				
				#send message of info through twilio!
				message = client.messages.create(
					from_=twilioSender,
					body=x["text"],
					to='[REDACTED]'
				)
				#End twilio stuff
		currentLocation[0] = newLocation[0]
		currentLocation[1] = newLocation[1]

