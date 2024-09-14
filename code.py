
import time
import board
from rainbowio import colorwheel

# Check the correct neopixel to use depending on the board
if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.3

r_value = 255 # set the initial R value in RGB

stage = 1 # save the stage of the story

break_time = 0.007 # speed of blinking

blink_time = 0 # save the number of blinks

while stage == 1: # first stage of the story
    led[0] = (r_value,0,0)
    time.sleep(break_time)
    r_value -= 1 # gradually decreasing RED color
    if r_value < 0: # go back to FULL RED and add one in the number of blinks
        print(blink_time)
        r_value = 255
        blink_time += 1
    if blink_time == 4: # increasing blinking frequency
        break_time = 0
    if blink_time == 8: # when it blinks 8 times, go to stage 2 and reset others
        stage = 2
        break_time = 0.007
        blink_time = 0

while stage == 2:
    led[0] = (255,255,255) # blinking among White, Red, and Blue
    time.sleep(0.1)
    led[0] = (0,0,255)
    time.sleep(0.1)
    led[0] = (255,0,0)
    time.sleep(0.1)
    blink_time += 1
    if blink_time == 10: # when it blinks 10 times, go to stage 3 and reset
        stage = 3
        blink_time = 0

while stage == 3:
    led[0] = (255,0,0)
    time.sleep(0.1)
    led[0] = (0,0,0)
    time.sleep(0.1)
    blink_time += 1
    if blink_time == 15:
        stage = 4

while stage == 4:
    led[0] = (r_value,0,0)
    time.sleep(break_time)
    r_value -= 1
    if r_value < 0:
        print(blink_time)
        r_value = 255

