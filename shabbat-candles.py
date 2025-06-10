import pygame


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
font = pygame.font.SysFont('Times New Roman', 30)  # Sets up the font and size

unlitCandles = pygame.image.load("sc-unlit.png")  # Custom image
unlitCandles = pygame.transform.scale(unlitCandles, (1487.5, 1925))
litCandles = pygame.image.load("sc-lit.png")  # Custom Image
litCandles = pygame.transform.scale(litCandles, (1487.5, 1925))

lightCandles = False

# The main program loop
while True:

    # Loop to allow the user to exit by pressing down the escape key and to check if the mouse has been clicked.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()

        if pygame.mouse.get_pressed()[0]:
            lightCandles = not lightCandles

    # Colors the screen white with the screenColor variable we defined earlier
    screen.fill(screenColor)

    if lightCandles:
        x = ((screen.get_width() - litCandles.get_width()) / 2).__ceil__()
        y = ((screen.get_height() - litCandles.get_height()) / 2).__ceil__()
        screen.blit(litCandles, (x, y))

    else:
        x = ((screen.get_width() - unlitCandles.get_width()) / 2).__ceil__()
        y = ((screen.get_height() - unlitCandles.get_height()) / 2).__ceil__()
        screen.blit(unlitCandles, (x, y))

    prayer = ("Baruch Atah Adonai, Eloheinu Melech haolam / Asher kid'shanu b'mitzvotav v'zivanu l'hadlik ner shel "
              "Shabbat (Amen)")

    prayerText = font.render(prayer, True, (0, 0, 0))

    # And then, we prepare a rectangular surface for the text to "rest" on:
    prayerX = (screen.get_rect().bottomright[0] / 2).__ceil__()  # Sets the x position of the rectangle
    prayerY = (screen.get_rect().bottomright[1] * 15 / 16).__ceil__()  # Sets the y position of the rectangle
    prayerRect = prayerText.get_rect()
    prayerRect.center = (prayerX, prayerY)

    screen.blit(prayerText, prayerRect)

    # Displays the final product of the window before it repeats the process
    pygame.display.flip()
