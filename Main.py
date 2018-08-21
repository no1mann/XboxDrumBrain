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

# Find drum joy stick
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
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print "Yep"
