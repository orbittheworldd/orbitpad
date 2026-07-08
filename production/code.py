# Firmware for orbittheworld's hackpad/macropad!

import board
import busio
import displayio
import adafruit_displayio_ssd1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.keys import Key
from subprocess import Popen
from kmk.extensions.display import Display, ImageEntry

# Setting up OLED Display
oled_i2c = io.I2C(sda=board.D4, scl=board.D5, frequency=400_000)
oled_display = Display(
    display=SSD1306(oled_i2c),
    width=128,
    height=32,
    flip=True,
    entries=[ImageEntry(0, 0, "dylansmacropad.bmp")],

# Custom key for youtube music
def openytmusic_on_press(key):
    Popen(['YouTube Music.exe'])

KC_ytm = Key(on_press=openytmusic_on_press)

# Custom key for discord
def opendiscord_on_press(key):
    Popen(['Discord.exe'])

KC_discord = Key(on_press=opendiscord_on_press)

# Custom key for steam
def opensteam_on_press(key):
    Popen(['steam.exe'])

KC_steam = Key(on_press=opensteam_on_press)


keyboard = KMKKeyboard()


# Button setup - 4 buttons on pins D0, D1, D2, D3
PINS = [board.D0, board.D1, board.D2, board.D3]

# Define what each key does
keyboard.keymap = [
    [
        KC.MUTE,      # pin D0
        KC_ytm,        # pin D1
        KC_discord,    # pin D2
        KC_steam,      # pin D3
    ]
]

if __name__ == "__main__":
    keyboard.go()

