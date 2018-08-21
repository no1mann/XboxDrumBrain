import pygame
import sys
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

# Main drum listening loop
while 1:
    clock.tick(100)
    list = []
    # Load button inputs
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            list.append(event.button+1)

    # Drum Buttons
    if 2 in list and 10 in list:
        print "Red Pad"
    if 4 in list and 6 in list:
        print "Yellow Cym"
    if 4 in list and 10 in list:
        print "Yellow Pad"
    if 3 in list and 6 in list:
        print "Blue Cym"
    if 3 in list and 10 in list:
        print "Blue Pad"
    if 1 in list and 6 in list:
        print "Green Cym"
    if 1 in list and 10 in list:
        print "Green Pad"
    if 5 in list:
        print "Kick"
