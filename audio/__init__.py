"""# audio conversion library.

Uses ffmpeg to convert input audio file to a numpy array

## Required Libraries
 - numpy
 - scipy

## Required Software
 - ffmpeg
"""

## Uncomment if you need to use just the audio module directly
# if __name__ == "__main__":
#     import sys
#     sys.path.append("..")

from spyctrum.audio.object import Audio

# expose frequency <-> note conversions at top level
from spyctrum.audio.notes import note_to_frequency, frequency_to_note
