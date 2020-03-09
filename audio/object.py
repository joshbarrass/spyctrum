import os

import numpy as np
from scipy.io import wavfile

from spyctrum.audio.reading import memread, tempread
from spyctrum.audio.fourier import get_chunk, ALIGN_CENTRAL

READ_MEMORY = 0
READ_TEMPFILE = 1

class Audio(object):
    def __init__(self, fp, method=READ_MEMORY):
        """wrapper for audio data to simplify storing and tracking

Args:
 - fp: string, path to audio file
 - method: int, either READ_MEMORY or READ_TEMPFILE. Specifies how the file
   will be read.
"""
        self.fp = os.path.abspath(os.path.expanduser(fp))
        if os.path.splitext(self.fp)[1].lower() == "wav":
            # don't need ffmpeg to read .wav, just use scipy directly
            self.rate, self.data = wavfile.read(self.fp)
        elif method == READ_MEMORY:
            self.rate, self.data = memread(self.fp)
        elif method == READ_TEMPFILE:
            self.rate, self.data = tempread(self.fp)
        else:
            raise ValueError("'method' should be either READ_MEMORY or READ_TEMPFILE")

    # TODO: currently the fourier output is complex, but the input
    # signal is real. Need to remove the complex part and the negative
    # frequencies
    def fourierChunk(self, timestamp, chunk_size, alignment=ALIGN_CENTRAL, mono=True):
        """Uses audio.fourier.get_chunk to get a chunk from the audio data and
perform the Fourier transform of it.

## Args:
 - timestamp: float, time from the start of the audio, in seconds, to
the point of about which you wish to sample
 - chunk_size: int, number of samples to include in the chunk
 - alignment: int, how to align the chunk to the timestamp. Default:
ALIGN_CENTRAL
 - mono: bool, whether to make the data mono before performing the FFT

## Returns:
 - freqdata: array, the FFT of the chunk of data. For an array
corresponding to the frequencies in this array, use Audio.fourierFreq

        """
        
        chunk = get_chunk(self.data, timestamp, self.rate, chunk_size, alignment)

        # add without averaging/normalising to avoid decreasing
        # amplitude of signal
        #
        # see https://stackoverflow.com/questions/23504901/convert-16-bit-stereo-sound-to-16-bit-mono-sound#comment36048770_23505029
        if mono:
            chunk = np.sum(chunk, axis=1)

        fftdata = np.fft.fft(chunk, axis=0)
        return fftdata

    def fourierFreq(self, chunk_size):
        """Returns the frequency array for a given chunk size

## Args:
 - chunk_size: int, number of samples in your chunk

## Returns:
 - f: array, contains the frequencies in the FFT
"""
        return np.fft.fftfreq(chunk_size, 1.0 / self.rate)
