from enum import *

# Colors of pads
class Colors(Enum):
    red = 2
    yellow = 4
    blue = 3
    green = 1
    orange = 5

# Types of drum pads
class PadType(Enum):
    pad = 10
    cymbol = 6

# POV controller mapping
class CymPOV(Enum):
    yellow_cym = 1
    blue_cym = -1