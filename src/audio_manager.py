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
# More channels are required when multiple pads are being hit
Mix_AllocateChannels(256)

# Default audio locations
AUDIO_FILE_LOCATION = "../audio/"
AUDIO_FILE_TYPE = ".wav"

# Enumeration of audio files loaded into memory
class Audio(Enum):
    red_pad = Mix_LoadWAV(byteify(''.join((AUDIO_FILE_LOCATION, "red_pad", AUDIO_FILE_TYPE)), "utf-8"))
    yellow_pad = Mix_LoadWAV(byteify(''.join((AUDIO_FILE_LOCATION, "yellow_pad", AUDIO_FILE_TYPE)), "utf-8"))
    yellow_cymbol = Mix_LoadWAV(byteify(''.join((AUDIO_FILE_LOCATION, "yellow_cymbol", AUDIO_FILE_TYPE)), "utf-8"))
    blue_pad = Mix_LoadWAV(byteify(''.join((AUDIO_FILE_LOCATION, "blue_pad", AUDIO_FILE_TYPE)), "utf-8"))
    blue_cymbol = Mix_LoadWAV(byteify(''.join((AUDIO_FILE_LOCATION, "blue_cymbol", AUDIO_FILE_TYPE)), "utf-8"))
    green_pad = Mix_LoadWAV(byteify(''.join((AUDIO_FILE_LOCATION, "green_pad", AUDIO_FILE_TYPE)), "utf-8"))
    green_cymbol = Mix_LoadWAV(byteify(''.join((AUDIO_FILE_LOCATION, "green_cymbol", AUDIO_FILE_TYPE)), "utf-8"))
    orange = Mix_LoadWAV(byteify(''.join((AUDIO_FILE_LOCATION, "orange", AUDIO_FILE_TYPE)), "utf-8"))

# Processing queue for audio files
sound_queue = Queue.Queue()

# Global thread for audio processing
def sound_thread():
    global sound_queue
    while 1:
        # If the audio processing queue is not empty, process the queue
        if not sound_queue.empty():
            # Every audio file in the queue
            for item in iter(sound_queue.get, None):
                # Launch new thread to play audio file
                thread.start_new_thread(play_sound, (item,))
            # Clear queue when processing is finished
            sound_queue = Queue.Queue()
        # Pause the thread for efficiency
        time.sleep(.01)

# Function for playing an individual audio file
def play_sound(audio):
    Mix_PlayChannel(-1, audio, 0)
