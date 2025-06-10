from ursina import *


app = Ursina(title="test-game", icon="iconV2.ico", borderless=False, size=[1000, 1000], fullscreen=False)

print("APP DEFINED : SUCCESS ")

# Setting the color of the window
window.color = color.hex("ffc5cb")

# Enabling the buttons we want and disabling the others
window.exit_button.enable()
window.fps_counter.disable()
window.collider_counter.disable()
window.entity_counter.disable()
window.cog_button.disable()

red = 0
green = 0
blue = 255

myVeryFirstEntity = Entity(model="cube",
                           color=color.rgb(red, green, blue),
                           texture="white_cube",
                           rotation=(50, 50, 50))


app.run()
