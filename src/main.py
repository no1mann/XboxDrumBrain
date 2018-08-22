import pygame
import sys
from audio_manager import *
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

# Starts the sound listening thread
thread.start_new_thread(sound_thread, ())

# MAIN DRUM LISTENING LOOP
while 1:
    button_list = []
    pov_list = []

    # Load button inputs
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            button_list.append(event.button + 1)
        if event.type == pygame.JOYHATMOTION:
            if event.value[1] != 0:
                pov_list.append(event.value[1])

    # Drum Buttons
    if Colors.red in button_list and PadType.pad in button_list:
        sound_queue.put(Audio.red_pad)
    if Colors.yellow in button_list and PadType.cymbol in button_list:
        sound_queue.put(Audio.yellow_cymbol)
    if Colors.yellow in button_list and PadType.pad in button_list:
        sound_queue.put(Audio.yellow_pad)
    if Colors.blue in button_list and PadType.cymbol in button_list:
        sound_queue.put(Audio.blue_cymbol)
    if Colors.blue in button_list and PadType.pad in button_list:
        sound_queue.put(Audio.blue_pad)
    if Colors.green in button_list and PadType.cymbol in button_list:
        sound_queue.put(Audio.green_cymbol)
    if Colors.green in button_list and PadType.pad in button_list:
        sound_queue.put(Audio.green_pad)
    if Colors.orange in button_list:
        sound_queue.put(Audio.orange)

    # Pause the thread for efficiency
    time.sleep(.02)
