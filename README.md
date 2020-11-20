### NukeGame
# Version 0.0a002
## Welcome to my Nuclear Triad Launch Systems CLI application. It is a simple sim that makes you enter a few digits into the CLI.
This is a very basic app and i wanna go back to it to improve it. 
my first goal is to actually develop the CLI with an ASCII Interface. To give it more of an interesting look. 
There are of course several pop references in the program to keep it light and not be a very official looking CLI. 
Afterwards i intend to develop it into a a simple GUI app with tkinter. 
For this i will need to work on the following stuff
* I need keep studying Python
* I need to learn OOP
* I need to edit the CLI app to shorter the amount of code lines. Through classes. 
* I need to edit the app to add ASSCII Intefaces. 
* I need to learn tkinter
* or other GUI framework
* Add media

#### These are the ones at most of the top of my head
I'll keep working on it through out on.
##### New Version released top level release notes
So after a taking another stab at at it through a few hours. I think the game can be considered different enough for a new "version" to be pushed to Git Hub.
This new version of the game "0.0a002" implements some clean up of the CLI text to separate each phase of the game into its separate text block. 
i also added a time delay to the processing of most printed text (i am interested in looking for a way to have previous print function outputs dissapear and the next print output follows where the previous one was. I want this for a loading screen effect).
Furthermore i decided to change the flow of the first few inputs. And allow for any kind of log in text to be inputted while still retaining some form of randomness in the acess of the rest of the body of the game. 
I added some more hacking/hackery dialoge in the print output of some of the statements. 

##### WE FOUND OUR FIRST GLITCH (OR SO WE SUSPECT)
Through personal testing and testing of another users, "Our closed Alpha team ;-p" We seem to have run into a glitch. Any time we ran into the permission/credential checker stage. Which you need to pass successfully to proceed to the main part of the game. We would be denied access, it seems that either the ratio of allowed entry tuples vs every other variable in the random.randrange() method was leaning too far into the denied range. And we were getting denied. So for enjoyability and playability i increased the permitted entry tuples that the credentials check function compares from, to allow it a greater range of addmitted variables.
I did try to maintain enough variability in the game to allow for some pretty interesting outcomes. 
also 
#### KEEP YOUR EYES ON THE GAME FOR POTENTIAL EASTER EGG =) 


