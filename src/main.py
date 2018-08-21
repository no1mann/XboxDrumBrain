import pygame
import sys
import Queue
import winsound
import thread
import time
from joystick_controls import *

pygame.init()

clock = pygame.time.Clock()
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

def sound_thread(arg):
    global sound_queue
    while 1:
        if not sound_queue.empty():
            for item in iter(sound_queue.get, None):
                winsound.PlaySound(item, winsound.SND_ASYNC)
            sound_queue = Queue.Queue()


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
