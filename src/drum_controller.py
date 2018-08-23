from joystick_controls import *
from audio_manager import *

def process_audio(item):
    thread.start_new_thread(play_sound, (item,))

def process_inputs(button_list, pov_list):
    # Drum Buttons
    if Colors.red in button_list and PadType.pad in button_list:
        process_audio(Audio.red_pad)
    if Colors.yellow in button_list and PadType.cymbol in button_list:
        process_audio(Audio.yellow_cymbol)
    if Colors.yellow in button_list and PadType.pad in button_list:
        process_audio(Audio.yellow_pad)
    if Colors.blue in button_list and PadType.cymbol in button_list:
        process_audio(Audio.blue_cymbol)
    if Colors.blue in button_list and PadType.pad in button_list:
        process_audio(Audio.blue_pad)
    if Colors.green in button_list and PadType.cymbol in button_list:
        process_audio(Audio.green_cymbol)
    if Colors.green in button_list and PadType.pad in button_list:
        process_audio(Audio.green_pad)
    if Colors.orange in button_list:
        process_audio(Audio.orange)
