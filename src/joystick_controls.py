from enum import *
from sdl2.ext.compat import byteify
from sdl2.sdlmixer import *

class Colors(Enum):
    red = 2
    yellow = 4
    blue = 3
    green = 1
    orange = 5

class PadType(Enum):
    pad = 10
    cymbol = 6

if Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 1024):
    raise RuntimeError("Cannot open mixed audio: {}".format(Mix_GetError()))

class Audio(Enum):
    red_pad = Mix_LoadWAV(byteify("../audio/red_pad.wav", "utf-8"))
    yellow_pad = Mix_LoadWAV(byteify("../audio/yellow_pad.wav", "utf-8"))
    yellow_cymbol = Mix_LoadWAV(byteify("../audio/yellow_cymbol.wav", "utf-8"))
    blue_pad = Mix_LoadWAV(byteify("../audio/blue_pad.wav", "utf-8"))
    blue_cymbol = Mix_LoadWAV(byteify("../audio/blue_cymbol.wav", "utf-8"))
    green_pad = Mix_LoadWAV(byteify("../audio/green_pad.wav", "utf-8"))
    green_cymbol = Mix_LoadWAV(byteify("../audio/green_cymbol.wav", "utf-8"))
    orange = Mix_LoadWAV(byteify("../audio/orange.wav", "utf-8"))
