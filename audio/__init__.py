"""# audio conversion library.

Uses ffmpeg to convert input audio file to a numpy array

## Required Libraries
 - numpy
 - scipy

## Required Software
 - ffmpeg
"""

## Uncomment if you need to use just the audio module
# if __name__ == "__main__":
#     import sys
#     sys.path.append("..")

from audio.reading import memread, tempread
