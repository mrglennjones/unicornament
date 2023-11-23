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

class frame:
    def __init__(self, frame_x, frame_y):
        self.frame_x = frame_x
        self.frame_y = frame_y

stockingframes = []
# describe as index from 0 - 3
stockingframes.append(frame (0, 0))
stockingframes.append(frame (1, 0))
stockingframes.append(frame (2, 0))
stockingframes.append(frame (3, 0))
stockingframes.append(frame (0, 0))
stockingframes.append(frame (1, 0))
stockingframes.append(frame (2, 0))
stockingframes.append(frame (3, 0))

santaframes = []
# describe as index from 0 - 3
santaframes.append(frame (0, 1))
santaframes.append(frame (1, 1))
santaframes.append(frame (2, 1))
santaframes.append(frame (3, 1))
santaframes.append(frame (0, 1))
santaframes.append(frame (1, 1))
santaframes.append(frame (2, 1))
santaframes.append(frame (3, 1))

snowmanframes = []
# describe as index from 0 - 3
snowmanframes.append(frame (0, 2))
snowmanframes.append(frame (1, 2))
snowmanframes.append(frame (2, 2))
snowmanframes.append(frame (3, 2))
snowmanframes.append(frame (0, 2))
snowmanframes.append(frame (1, 2))
snowmanframes.append(frame (2, 2))
snowmanframes.append(frame (3, 2))

snowflakeframes = []
# describe as index from 0 - 3
snowflakeframes.append(frame (0, 3))
snowflakeframes.append(frame (1, 3))
snowflakeframes.append(frame (2, 3))
snowflakeframes.append(frame (3, 3))
snowflakeframes.append(frame (0, 3))
snowflakeframes.append(frame (1, 3))
snowflakeframes.append(frame (2, 3))
snowflakeframes.append(frame (3, 3))

candycaneframes = []
# describe as index from 0 - 3
candycaneframes.append(frame (0, 4))
candycaneframes.append(frame (1, 4))
candycaneframes.append(frame (2, 4))
candycaneframes.append(frame (3, 4))
candycaneframes.append(frame (3, 4))
candycaneframes.append(frame (2, 4))
candycaneframes.append(frame (1, 4))
candycaneframes.append(frame (0, 4))

hollyframes = []
# describe as index from 0 - 3
hollyframes.append(frame (0, 5))
hollyframes.append(frame (1, 5))
hollyframes.append(frame (2, 5))
hollyframes.append(frame (3, 5))
hollyframes.append(frame (3, 5))
hollyframes.append(frame (2, 5))
hollyframes.append(frame (1, 5))
hollyframes.append(frame (0, 5))

mistletoeframes = []
# describe as index from 0 - 3
mistletoeframes.append(frame (0, 6))
mistletoeframes.append(frame (1, 6))
mistletoeframes.append(frame (2, 6))
mistletoeframes.append(frame (3, 6))
mistletoeframes.append(frame (3, 6))
mistletoeframes.append(frame (2, 6))
mistletoeframes.append(frame (1, 6))
mistletoeframes.append(frame (0, 6))

baubleframes = []
# describe as index from 0 - 3
baubleframes.append(frame (0, 7))
baubleframes.append(frame (1, 7))
baubleframes.append(frame (2, 7))
baubleframes.append(frame (3, 7))
baubleframes.append(frame (0, 7))
baubleframes.append(frame (1, 7))
baubleframes.append(frame (2, 7))
baubleframes.append(frame (3, 7))

faceframes =["stockingframes", "santaframes", "snowmanframes", "snowflakeframes", "candycaneframes", "hollyframes", "mistletoeframes", "baubleframes"]

selected_frame = random.choice(faceframes)
print(f"Selected frame: {selected_frame}")

busy = False

def JumpScare():
    global busy
    #gu.set_brightness(max(.15,min(1.,gu.light()/100)))
    busy = True
    #gu.set_volume(0.1)
    #play random sound
    ####wp.play('laugh/LAUGH-1.wav', loop=1)
    #wp.play(random.choice(LAUGH_SOUND), loop=1)

    #pick random face
    selected_frame = random.choice(faceframes)
    print(f"Selected frame: {selected_frame}")
    # Use the correct list of frames based on selected_frame
    if selected_frame == "stockingframes":
        frame_list = stockingframes
    elif selected_frame == "santaframes":
        frame_list = santaframes
    elif selected_frame == "snowmanframes":
        frame_list = snowmanframes
    elif selected_frame == "snowflakeframes":
        frame_list = snowflakeframes
    elif selected_frame == "candycaneframes":
        frame_list = candycaneframes
    elif selected_frame == "hollyframes":
        frame_list = hollyframes
    elif selected_frame == "mistletoeframes":
        frame_list = mistletoeframes
    elif selected_frame == "baubleframes":
        frame_list = baubleframes
    else:
        frame_list = []  # Handle the case when selected_frame is invalid


    # set initial brightness to 0
    brightness = 0
    gu.set_brightness(brightness)

    for index, frame in enumerate(frame_list):

        # Clear the display before drawing the new frame
        graphics.set_pen(black)
        graphics.clear()

        # Decode and display the current frame
        png.decode(0, 0, source=(frame.frame_x * frame_width, frame.frame_y * frame_height, frame_width, frame_height), scale=(1, 1), rotate=0)

        gu.update(graphics)

        if index == 0:
            for _ in range(10):
                brightness += 0.1
                gu.set_brightness(brightness)
                gu.update(graphics)
                time.sleep(0.01)

        elif index == 7:
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

