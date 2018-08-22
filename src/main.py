import os
os.environ["PYSDL2_DLL_PATH"] = "\\"

import pygame
import sys
import Queue
import thread
import time
from sdl2 import *
from joystick_controls import *

pygame.init()

joysticks = []
drum_joystick = None

# Load all joysticks
print "Listing all joysticks..."
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[i].init()
    print "Joystick #%d: %s" % (i, joysticks[-1].get_name())

print ""

# Find drum joystick
for joy in joysticks:
    if "drum" in joy.get_name().lower():
        print "Drum Kit Found... (%s)" % (joy.get_name())
        drum_joystick = joy
    else:
        joy.quit()

# If a drum joystick was found, use it
if drum_joystick is None:
    print "Drum Kit not found."
    sys.exit()

sound_queue = Queue.Queue()

if SDL_Init(SDL_INIT_AUDIO) != 0:
    raise RuntimeError("Cannot initialize audio system: {}".format(SDL_GetError()))

Mix_AllocateChannels(256)
def play_sound(sample):
    channel = Mix_PlayChannel(-1, sample, 0)

def sound_thread(arg):
    global sound_queue
    while 1:
        if not sound_queue.empty():
            for item in iter(sound_queue.get, None):
                thread.start_new_thread(play_sound, (item,))
            sound_queue = Queue.Queue()
        time.sleep(.01)


thread.start_new_thread(sound_thread, ("thread1", ))

# Main drum listening loop
while 1:
    list = []
    # Load button inputs
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            list.append(event.button+1)

    # Drum Buttons
    if Colors.red in list and PadType.pad in list:
        sound_queue.put(Audio.red_pad)
    if Colors.yellow in list and PadType.cymbol in list:
        sound_queue.put(Audio.yellow_cymbol)
    if Colors.yellow in list and PadType.pad in list:
        sound_queue.put(Audio.yellow_pad)
    if Colors.blue in list and PadType.cymbol in list:
        sound_queue.put(Audio.blue_cymbol)
    if Colors.blue in list and PadType.pad in list:
        sound_queue.put(Audio.blue_pad)
    if Colors.green in list and PadType.cymbol in list:
        sound_queue.put(Audio.green_cymbol)
    if Colors.green in list and PadType.pad in list:
        sound_queue.put(Audio.green_pad)
    if Colors.orange in list:
        sound_queue.put(Audio.orange)
    time.sleep(.02)
