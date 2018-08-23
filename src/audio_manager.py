import os
os.environ["PYSDL2_DLL_PATH"] = "\\"

import Queue
import thread
import time
from enum import *
from sdl2 import *
from sdl2.ext.compat import byteify
from sdl2.sdlmixer import *

# Initializes SDL audio library
if SDL_Init(SDL_INIT_AUDIO) != 0:
    raise RuntimeError("Failed to initialize audio system: {}".format(SDL_GetError()))

# Opens audio stream
if Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 1024):
    raise RuntimeError("Failed to open mixed audio: {}".format(Mix_GetError()))

# Allocates audio channels for mixing. An individual audio channel plays 1 audio clip.
# More channels are required when multiple pads are being hit at the same time
Mix_AllocateChannels(256)

# Default audio locations
AUDIO_FILE_LOCATION = "../audio/"
AUDIO_FILE_TYPE = ".wav"

# Function for loading audio files into memory
def load_audio(file_name):
    return Mix_LoadWAV(byteify(''.join((AUDIO_FILE_LOCATION, file_name, AUDIO_FILE_TYPE)), "utf-8"))

# Enumeration of audio files loaded into memory
class Audio(Enum):
    red_pad = load_audio("red_pad")
    yellow_pad = load_audio("yellow_pad")
    yellow_cymbol = load_audio("yellow_cymbol")
    blue_pad = load_audio("blue_pad")
    blue_cymbol = load_audio("blue_cymbol")
    green_pad = load_audio("green_pad")
    green_cymbol = load_audio("green_cymbol")
    orange = load_audio("orange")

# Function for playing an individual audio file
def play_sound(audio):
    Mix_PlayChannel(-1, audio, 0)
