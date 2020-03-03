import numpy as np

ALIGN_CENTRAL = 0
ALIGN_START = 1
ALIGN_END = 2

def get_chunk(a, timestamp, sample_rate, chunk_size, alignment=ALIGN_CENTRAL):
    """get_chunk takes an array and returns a chunk to be analysed

## Args:
 - a: array-like, signal to be analysed
 - timestamp: float, time from the start of the signal, in seconds, to the
   point about which you wish to sample
 - sample_rate: float, sample rate of the signal
 - chunk_size: int, number of samples to include in the chunk
 - alignment: int, how to align the chunk to the timestamp

## Returns:
 - chunk: array, the chunk of data to be analysed
    """
    if isinstance(a, (tuple, list)):
        length = len(a)
    if isinstance(a, np.ndarray):
        length = a.shape[0]

    target = int(sample_rate * timestamp)
    if alignment == ALIGN_CENTRAL:
        split, rem = divmod(chunk_size, 2)
        top = max(target - split, 0)
        bottom = min(target + split + rem, length)
    elif alignment == ALIGN_START:
        top = max(target, 0)
        bottom = min(target + chunk_size, length)
    elif alignment == ALIGN_END:
        top = max(target - chunk_size + 1, 0)
        bottom = min(target + 1, length)
    else:
        raise ValueError("invalid value for 'alignment'") 

    return a[top:bottom]
