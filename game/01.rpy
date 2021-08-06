# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:

   # Show a background. This uses a placeholder by default, but you can
   # add a file (named either "bg room.png" or "bg room.jpg") to the
   # images directory to show it.
   window auto 
   scene turtle01 with fade:
      yalign 0.0
      linear 15.0 yalign 0.6
   pause

   # This shows a character sprite. A placeholder is used, but you can
   # replace it by adding a file named "eileen happy.png" to the images
   # directory.

   # These display lines of dialogue.

   "2020 was a year of disasters.
   {w}We had a very hot summer in Australia which resulted in the country’s worst bushfires in a hundred years." 
   "The constant heat made me antsy and a bit cranky."
   nvl clear 
   "No sooner had the fires been extinguished than we were all hit with COVID-19, lock-downs, and restrictions. "
   "At least the shortages in supermarkets didn’t affect me as I was already well-provisioned when the pandemic hit."
   "Being cooped up at home with no place to go, though, like millions of others, drove me crazy.{w} I’m young and I’m lonely."
   nvl clear 
   "I decided that I needed a getaway."
   "Leaving my home is not something I do often, nor do I do it lightly." 
   "I have very special needs and my home is very comfortable.{w} Leaving it requires exposing myself to the perils of the outside world."
   
   "I’m George, an Australian Long-necked Turtle,{w} and my home is one meter by four meter pond in Adelaide,{w} South Australia."
   nvl clear 

   "I felt an overwhelming desire to find a girlfriend,{w} though,{w} but my search needed to be executed carefully."
   "First,{w} my owner needed to fill my pond up to the very top.{w} Otherwise, it would be impossible for me to climb over the steep concrete sides."
   "Secondly,{w} I needed them to leave a crucial door open or I would be trapped inside a courtyard."
   "It was pointless leaving my home only to be trapped,{w} as I knew I would never find a girlfriend in the courtyard."
   nvl clear 
   scene turtle02 with dissolve:
      yalign 0.6
      linear 15.0 yalign 0.0

   "The day finally arrived."
   "My owner had filled up my pond to the brim the night before and accidentally left the door open." 
   "I could sense that it was going to be a hot day,{w} so I climbed out at first light to make an early start." 
   "The first part of my journey involved crossing a giant wooden structure—my owner referred to as a deck."
   nvl clear 
   "Although I felt very exposed, I knew that I could always retreat inside my shell if I was threatened."
   "I much prefer swimming to walking. The wooden surface was hot and hard and it took me a long time to reach the other side.
   I finally reached an expanse of native ground cover which was gentle to the touch and much cooler."
   "Botanists refer to it as dichondra repens, but my owner called it Tom Thumb."
   nvl clear
   "As I crossed it, I disturbed a piping shrike having a bath but, fortunately, she was more interested in staying cool than pecking me."

   # This ends the game.

   return
