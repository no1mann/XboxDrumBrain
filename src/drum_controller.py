from joystick_controls import *
from audio_manager import *

# Starts the sound listening thread
thread.start_new_thread(sound_thread, ())

def process_inputs(button_list, pov_list):
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