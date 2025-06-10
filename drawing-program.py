"""
Written in February and March 2025 by Noga Levy.

This program creates a (computer) window on which the user can draw on.
"""

import pygame


# Returns a list with the X and Y coordinates at that specific moment
def find_position():
    pointer_pos = pygame.mouse.get_pos()
    return [pointer_pos[0], pointer_pos[1]]


# Returns the original color value plus 5
def change_color(color):
    if color + 5 <= 255:
        color += 5
    else:
        color = 0

    return color


# Initializes a blank window
pygame.init()
screen = pygame.display.set_mode()
# Sets the tuple for the screen color--will be used near the beginning of the "while running: ..." loop
screenColor = (255, 255, 255)  # Written in RGB numbers

# Set the CHANGEABLE list value for the circle-pointer tuple. It will be used in the main program loop of
# "while running: ..."
pointerColor = [0, 0, 0]

# Colors the screen white with the screenColor variable we defined earlier
screen.fill(screenColor)

# Now, we are going to make instructions for the user.

# We start by making the variable containing the text:
instructions = "Tip: Keys R, G, and B add 5 to the RGB values of the paint, respectively. Press Esc to leave."

# Then, we initialize the font (which will also be used later)
font = pygame.font.SysFont('Times New Roman', 32)  # Sets up the font and size

# Next, we render all the elements of the text (without the background, as it is unnecessary for this)
instructionalText = font.render(instructions, True, (0, 0, 0))

# And then, we prepare a rectangular surface for the text to "rest" on:
instructionalX = (screen.get_rect().bottomright[0]/2).__ceil__()  # Sets the x position of the rectangle
instructionalY = (screen.get_rect().bottomright[1] * 15/16).__ceil__()  # Sets the y position of the rectangle
instructionalRect = instructionalText.get_rect()
instructionalRect.center = (instructionalX, instructionalY)

# Finally, we put it on the screen--not in the loop so that the user can draw over it.
screen.blit(instructionalText, instructionalRect)

# Variable that will control the program running
running = True

# The main program loop
while running:

    # Loop to allow the user to modify the color of their paint or exit the program all together.
    for event in pygame.event.get():

        # Checks if the user wants to exit
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        # The three elif statements check to see if the user wants to modify the R, G, or B values, respectively

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            pointerColor[0] = change_color(pointerColor[0])

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            pointerColor[1] = change_color(pointerColor[1])

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            pointerColor[2] = change_color(pointerColor[2])

    # String containing the message displaying the RBG values of the paint
    RBG_str = f"   R = {pointerColor[0]}, G = {pointerColor[1]}, B = {pointerColor[2]}   "
    # Quick explanation of the spaces: the surface of the text paints the area white--if the area it covers is too
    # small, some of the previous message might be shown. The spaces are to ensure that scenario never happens.

    # We prepare the text, setting up the position and color (this time with a background so to make it look marginally
    # better)
    text = font.render(RBG_str, True, (0, 0, 0), (255, 255, 255))

    # Again, we prepare the surface/rectangle the text will be on
    textRectX = int(screen.get_rect().bottomright[0]/10) + len(RBG_str)
    textRectY = (screen.get_rect().bottomright[1]/19).__ceil__()
    textRect = text.get_rect()
    textRect.center = (textRectX, textRectY)  # The len() accounts for the message changing length, ensuring that none
    # of the characters get pushed off the field of vision.

    # And finally, we copy the prepared text, and it's surface once more to the surface, except this time, it can't be
    # drawn over
    screen.blit(text, textRect)

    # Initializes a tuple with the states (pressed = True, not pressed = False) of the mouse buttons
    buttonsPressed = pygame.mouse.get_pressed()

    if buttonsPressed[0]:
        # Draws the pointer-circle onto the screen
        pygame.draw.circle(screen, pointerColor, (find_position()[0], find_position()[1]), 15, 0)

    # Displays the final product of the window before it repeats the process
    pygame.display.flip()
