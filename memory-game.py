"""
Written March 2025 by Noga Levy.

This is the code for a memory game. It creates a blank, white window encompassing the entire screen, and in the middle,
there is a random food, chosen from the list "dishes." The user then presses the space bar to hide the word with a black
rectangle, and later on, presses the Esc button to exit the window. Once the window is gone, the user is prompted in the
terminal to input the dish name to see if they remember it. The program then responds with either a congregational
message or a disappointed one containing the answer, depending on if the user was correct or not.
"""

import pygame
import random


dishes = [
    "Spaghetti Bolognese", "Chicken Alfredo", "Margherita Pizza", "Cheeseburger", "Sushi Roll", "Tacos al Pastor",
    "Pad Thai", "Beef Stroganoff", "Eggplant Parmesan", "Shrimp Scampi", "Chicken Tikka Masala", "Lobster Bisque",
    "Clam Chowder", "French Onion Soup", "Caesar Salad", "Greek Salad", "Cobb Salad", "Caprese Salad", "Lasagna",
    "Mac and Cheese", "Buffalo Wings", "BBQ Ribs", "Pulled Pork Sandwich", "Philly Cheesesteak", "Reuben Sandwich",
    "Grilled Cheese", "Chicken and Waffles", "Biscuits and Gravy", "Cornbread", "Jambalaya", "Gumbo", "Po' Boy",
    "Hush Puppies", "Fried Green Tomatoes", "Shepherd's Pie", "Bangers and Mash", "Fish and Chips", "Beef Wellington",
    "Yorkshire Pudding", "Croissant", "Paella", "Gazpacho", "Churros", "Ratatouille", "Avocado Toast",
    "Scrambled Egg", "Mango Lassi", "Meatloaf", "Chocolate Mousse", "Gyro", "Tomato Soup", "Spanakopita",
    "Chicken Soup", "Falafel", "Shakshuka", "Hummus", "Baba Ganoush", "Panini", "Kebab", "Biryani", "Butter Chicken",
    "Bagel Bites", "Saag Paneer", "Salad Roll", "Samosa", "Naan", "Vindaloo", "Pho", "Banh Mi", "Spring Rolls",
    "Peking Duck", "Kung Pao Chicken", "Sweet and Sour Pork", "General Tso's Chicken", "Mapo Tofu", "Dumplings",
    "Hot Pot", "Gimbap", "Kimchi", "Bulgogi", "Japchae", "Momos", "Refried Beans", "Biancomangiare", "Enchiladas",
    "Fajitas", "Quesadilla", "Empanadas", "Pancakes", "Ceviche", "Katsu Curry", "Lobster Roll", "Tzatziki", "Mocha",
    "Gnocchi", "Risotto", "Pasta Salad", "Frittata", "Carbonara", "Tiramisu"
]


def text(words, bg):
    # We start by initializing the font
    font = pygame.font.SysFont('Times New Roman', 32)  # Sets up the font and size

    # Next, we render all the elements of the text (the bg will later have to be switched, so we it a parameter)
    words_text = font.render(words, True, (0, 0, 0), bg)  # The text is a parameter just because it makes
    # the code more readable

    # And then, we prepare a rectangular surface for the text to "rest" on:
    words_x = (screen.get_rect().bottomright[0] / 2).__ceil__()  # Sets the x position of the rectangle
    words_y = (screen.get_rect().bottomright[1] / 2).__ceil__()  # Sets the y position of the rectangle
    words_rect = words_text.get_rect()
    words_rect.center = (words_x, words_y)

    # Finally, we put it on the screen--not in the loop so that the user can draw over it.
    screen.blit(words_text, words_rect)


# We now initialize a blank window
pygame.init()
screen = pygame.display.set_mode()
screenColor = (255, 255, 255)  # Written in RGB numbers

# This colors the screen white with the screenColor variable we defined earlier
screen.fill(screenColor)

# We choose a random dish now from the "dishes" list. This will be what the user will have to remember
chosenWord = dishes[random.randint(0, len(dishes) - 1)]

# Since we now have our word, we can put it on the scree
text(chosenWord, (255, 255, 255))

# Refreshes the screen with the new information
pygame.display.flip()

# Prepares the variable that will keep the window up
running = True

spaceClicked = False

# The screen loop
while running:

    # Loop to allow the user to modify the color of their paint or exit the program all together.
    for event in pygame.event.get():

        # Checks if the user wants to exit
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
                and spaceClicked):
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not spaceClicked:
            text(chosenWord, (0, 0, 0))
            spaceClicked = True
            pygame.display.flip()


wordRemembered = input("What was the word that was on the screen? Enter here: ")

if wordRemembered.lower() == chosenWord.lower():
    print("Good job! That's correct")

else:
    print(f"Aw man, that's wrong... it was {chosenWord}.")
