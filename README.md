# XboxDrumBrain - A Virtural Drum Brain # 
Turn your Rock Band Xbox 360 drum controller into a realtime personal drum kit. Just plug your USB drum kit into your PC and run this program to start jamming out. This application was tested on a Windows 10 PC with an Xbox 360 Ion Drum Kit. 

## Configuration
Any other controller, including Guitar Hero drums and other console controllers, can be modified to work by changing the ```joystick_controls.py``` enumeration values.

Want a different drum sound? Replace the corresponding wav files in the ```\audio``` folder with the updated audio files. 

## Dependencies 
- [PySDL2](https://pysdl2.readthedocs.io/en/rel_0_9_6/) - A wrapper around the SDL2 library. Used for audio processing.
- [pygame](https://www.pygame.org/) - Full Python gaming library. Handles controller inputs.

