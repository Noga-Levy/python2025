"""
Written on February and March 2025, by Noga Levy.

This program creates a white window, using pygame, with a dot pointing to where the cursor is and some text
underneath displaying the X and Y coordinates of the mouse.

Credits:
Text displaying code ~ https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
"""

import pygame


# Returns a list with the X and Y coordinates at that specific moment
def find_position():
    pointer_pos = pygame.mouse.get_pos()
    return [pointer_pos[0], pointer_pos[1]]


# Initializes a blank window
pygame.init()
screen = pygame.display.set_mode()
# Sets the tuple for the screen color--will be used near the beginning of the "while running: ..." loop
screenColor = (255, 255, 255)

# Set the tuple for the circle-pointer tuple. It will be used in the main program loop of "while running: ..."
pointerColor = (0, 0, 0)

# Sets the tuple for the text color
blackText = (0, 0, 0)

# Prepares the font used in the while True loop
font = pygame.font.SysFont('Times New Roman', 32)  # Sets up the font and size

# The main program loop
while True:

    # Loop to allow the user to exit by pressing down the escape key.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()

    # Colors the screen white with the screenColor variable we defined earlier
    screen.fill(screenColor)

    # Draws the red rectangles used to help visualize where are the x and y
    thickness = 10  # Sets up the thickness

    pygame.draw.rect(screen, (255, 0, 0), (find_position()[0] - thickness/2, 0, thickness,
                                           screen.get_height()))  # Thickness must be accounted for in the X value

    pygame.draw.rect(screen, (255, 0, 0), (0, find_position()[1] - thickness/2, screen.get_width(),
                                           thickness))  # Thickness must be accounted for in the Y value

    text = font.render(f"x = {find_position()[0]}, y = {find_position()[1]}", True, blackText)  # Sets up
    # what the text will say

    # Prepares the surface/rectangle the text will be on

    textX = find_position()[0]  # Base X if the mouse isn't near the edges
    textY = find_position()[1] + int(screen.get_height()/20)  # Base Y if the mouse isn't near the edges

    # Sets the values that will define when the text is too close to the edges
    minimumX = screen.get_width() * 3/50
    maximumX = screen.get_width() * 93/100
    maximumY = screen.get_height() * 93/100

    # Checks to see if the mouse is near the edges and moves the position of the text accordingly so that it doesn't
    # get cut-off.
    if find_position()[0] <= minimumX:
        textX = find_position()[0] + int(screen.get_width() * 2/25)

    elif find_position()[0] >= maximumX:
        textX = find_position()[0] - int(screen.get_width() * 2/25)

    if find_position()[1] >= maximumY:
        textY = find_position()[1] - int(screen.get_height()/20)

    textRect = text.get_rect()
    textRect.center = (int(textX), int(textY))

    # Copies the prepared text and it's surface
    screen.blit(text, textRect)

    # Draws the pointer-circle onto the screen
    pygame.draw.circle(screen, pointerColor, (find_position()[0], find_position()[1]), 15, 0)

    # Displays the final product of the window before it repeats the process
    pygame.display.flip()
