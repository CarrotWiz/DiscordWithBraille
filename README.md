## NOTE: README.md is currently still incomplete

# DiscordWithBraille

Project for Ohio State University's BioHack 2021. Based off of a prompt provided by MedForAll.

## Description

A braille translator that is able to read messages from a Discord channel and out puts it to an LED display from an arduino.
Also uses 8 keys on a keyboard to represent a braille keyboard, which then can be used to send messages to the discord channel.

## Getting Started

### Installing

The following libraries will need to be installed to run the python files.

```
pip install keyboard
pip install requests
pip install pyserial
```

For Arduino, LEDMatrixDriver will need to be installed.

Tools > Manage Libraries... > LEDMatrixDriver > Install

## Acknowledgments

- https://github.com/bartoszbielawski/LEDMatrixDriver/blob/master/examples/DrawSprites/DrawSprites.ino 
- https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0 
- https://pyserial.readthedocs.io/en/latest/pyserial_api.html 
- http://timgolden.me.uk/pywin32-docs/win32gui.html 
- https://www.youtube.com/watch?v=xh28F6f-Cds 
- https://www.youtube.com/watch?v=DArlLAq56Mo
