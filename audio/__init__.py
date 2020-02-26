"""audio conversion library.

Uses ffmpeg to convert input audio file to a numpy array

Required Libraries:
 - numpy
 - scipy

Required Software:
 - ffmpeg
"""

if __name__ == "__main__":
    import sys
    sys.path.append("..")

from audio.reading import memread, tempread
