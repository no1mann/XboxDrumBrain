from enum import *
import wave

class Colors(Enum):
    red = 2
    yellow = 4
    blue = 3
    green = 1
    orange = 5

class PadType(Enum):
    pad = 10
    cymbol = 6

class Audio(Enum):
    red_pad = "../audio/red_pad.wav"
    yellow_pad = "../audio/yellow_pad.wav"
    yellow_cymbol = "../audio/yellow_cymbol.wav"
    blue_pad = "../audio/blue_pad.wav"
    blue_cymbol = "../audio/blue_cymbol.wav"
    green_pad = "../audio/green_pad.wav"
    green_cymbol = "../audio/green_cymbol.wav"
    orange = "../audio/orange.wav"
