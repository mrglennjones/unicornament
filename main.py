import time
import ntptime
import urequests
import random
import os
from cosmic import CosmicUnicorn
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN
from wave_player import WavePlayer
from pngdec import PNG
from machine import Pin

graphics = PicoGraphics(display=DISPLAY_COSMIC_UNICORN)
gu = CosmicUnicorn()

#Setup PIR Sensor
#PINS_BREAKOUT_GARDEN = {"sda": 4, "scl": 5}
pir =  machine.Pin(5)


gu.set_brightness(1)

wp = WavePlayer(gu)

png = PNG(graphics)
#png.open_file("/s4m_ur4i-pirate-characters.png")
png.open_file("/faces.png")

gu.set_volume(0.1)
LAUGH_SOUND = [ 'laugh/%s'%f for f in os.listdir('laugh') ]
print (LAUGH_SOUND)


frame_width = 32
frame_height = 32

black = graphics.create_pen(0,0,0)

anims = [
            [0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3],
            [0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3],
            [0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3],
            [0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3],
            [0,1,2,3,3,2,1,0,0,1,2,3,3,2,1,0],
            [0,1,2,3,3,2,1,0,0,1,2,3,3,2,1,0],
            [0,1,2,3,3,2,1,0,0,1,2,3,3,2,1,0],
            [0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]
        ]

busy = False

def JumpScare():
    global busy
    #gu.set_brightness(max(.15,min(1.,gu.light()/100)))
    busy = True
    #gu.set_volume(0.1)
    #play random sound
    ####wp.play('laugh/LAUGH-1.wav', loop=1)
    #wp.play(random.choice(LAUGH_SOUND), loop=1)

    #pick random anim
    selected_anim_number = random.randint(0, len(anims))
    selected_anim = anims[selected_anim_number]
    frame_count = len(selected_anim)

    print(f"Selected frame: {selected_anim_number}")

    # set initial brightness to 0
    brightness = 0
    gu.set_brightness(brightness)
    gu.update(graphics)

    for index in range(frame_count):

        # Clear the display before drawing the new frame
        graphics.set_pen(black)
        graphics.clear()

        frame = selected_anim[index]

        # Decode and display the current frame
        png.decode(0, 0, source=(frame * frame_width, selected_anim_number * frame_height, frame_width, frame_height), scale=(1, 1), rotate=0)

        gu.update(graphics)

        if index < 2:
            for _ in range(10):
                brightness += 0.1
                gu.set_brightness(brightness)
                gu.update(graphics)
                time.sleep(0.01)

        elif index > frame_count - 3:
            for _ in range(10):
                brightness -= 0.1
                gu.set_brightness(brightness)
                gu.update(graphics)
                time.sleep(0.01)

        else:
            time.sleep(0.1)  # Adjust speed of anim

    # Clear display
    graphics.set_pen(black)
    graphics.clear()
    gu.update(graphics)

    time.sleep(5) # Time out so it does not trigger again immediately

    busy = False


while True:
    #if gu.is_pressed(CosmicUnicorn.Sbauble_A):
    if pir.value() == 1:
        if not busy:
            JumpScare()





