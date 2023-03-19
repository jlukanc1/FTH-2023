# FTH-2023
Fashion-Tech-Hackathon 2023

# Requirements
Designed for Raspberry Pi 3 (GPIO use)
Requires (pip) python-vlc, twilio

Hardware: 3 pushbuttons, and a switch for "location", as well as speakers and wires of course.

# Code
The porgram is broken up into three main components. These include handling button input, playing songs from a predetermined list, and actions based on the current location of the user
## button handling
It uses the build-in GPIO library included with the Raspberry Pi to read the inputs from the buttons themselves. The prototype inlcudes three buttons. One button is used for playing or pausing music. The other two buttons are used for playing the next or previous song. 
## playing from a predeterminded list
There is a list of songs containing the full paths of their location on the system. Then the system is first started, it loads the first song from the list into the VLC media
