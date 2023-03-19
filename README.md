# FTH-2023
Fashion-Tech-Hackathon 2023

# Requirements
Designed for Raspberry Pi 3 (GPIO use)
Requires (pip) python-vlc, twilio

Hardware: 3 pushbuttons, and a switch for "location", as well as speakers and wires of course.

# Code
The program is broken up into three main components. These include handling button input, playing songs from a predetermined list, and actions based on the current location of the user
## Button Handling
It uses the built-in GPIO library included with the Raspberry Pi to read the inputs from the buttons themselves. The prototype includes three buttons. One button is used for playing or pausing music. The other two buttons are used for playing the next or previous song. 
## Playing From A Predetermined List
There is a list of songs containing the full paths of their location on the system. Then the system is first started, it loads the first song from the list into the VLC media player. Then the next or previous buttons are pressed, it stops the current song and gets either the next for previous song in the list. It uses the idea of circular arrays where the list cycles back to the beginning.
## Actions Based On Location Of The User
The program can load a location structure from a separate file. This structure has text to send to their user, the location, and an audio file.
```code
testStruct = {
  "text": "Text to be sent to user",
  "coords": [longitude, latitude],
  "file": "path to audio file"
}
```
These structures are stored in a list of locations to check. The system constantly checks its location and if its location changed, it will compare it with the locations from the structures.
If it finds a match, it will retrieve its audio file and start playing it.It also sends the message stored in its text variable to the user via text message. It does this via twilio. This allows for both audio output and textual information to be given to the user depending on their location.
