"""
What you've installed to get this to work:
- Pyscreeze (pre-installed, used for pyautogui locating feature)
- Pillow (PIL, used to get pyscreeze to work)
- OpenCV (cv2, used to get confidence in the pyautogui locate feature. Confidence is NECESSARY for locate to find the
  OBS symbol, as it is small and rather pixelated)
"""
import os
import pyautogui
import pygame


def open_obs():
    try:
        find_obs = pyautogui.locateCenterOnScreen(r"C:\Users\Noga\OneDrive\Pictures\Screenshots\Pick your poison "
                                                  r"of OBS images\obs-open.png", minSearchTime=0, confidence=0.8)

    except pyautogui.ImageNotFoundException:
        os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OBS Studio\OBS Studio (64bit).lnk")

    else:
        pyautogui.click(find_obs)


inMeet = False
talking = "Something went wrong with the \"while not inMeet\" loop. Variable \"talking\" didn't get defined."

while not inMeet:
    try:
        pyautogui.locateOnScreen(r"C:\Users\Noga\OneDrive\Pictures\Screenshots\Google Meet\mute.png",
                                 grayscale=False, confidence=0.9)

    except pyautogui.ImageNotFoundException:

        try:
            pyautogui.locateOnScreen(r"C:\Users\Noga\OneDrive\Pictures\Screenshots\Google Meet\unmute.png",
                                     confidence=0.9)

        except pyautogui.ImageNotFoundException:
            continue

        else:
            inMeet = True
            talking = True

    else:
        inMeet = True
        talking = False

pygame.init()

while True:

    # Loop to allow the user to exit by pressing down the escape key.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()

    try:
        pyautogui.locateOnScreen(r"C:\Users\Noga\OneDrive\Pictures\Screenshots\Google Meet\mute.png",
                                 grayscale=False, confidence=0.9)

    except pyautogui.ImageNotFoundException:  # This means Google Meet is unmuted
        if not talking:  # If the last time we checked, we weren't talking (AKA Google Meet was muted), then set OBS to
            # unmute
            talking = True
            open_obs()
            # TODO: Insert code to unmute OBS

    else:  # This means Google Meet is muted
        if talking:  # If the last time we checked, we were talking (AKA Google Meet was unmuted), then set OBS to mute
            talking = False
            open_obs()
            # TODO: Insert code to mute OBS
