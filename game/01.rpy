# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene turtle1.png with fade#:

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
    # This ends the game.

    return
