def fix_RIFF_chunk_sizes(data):
    """Need to manually fix RIFF chunk size when using output piped from
ffmpeg. See https://github.com/kkroening/ffmpeg-python/issues/118

    """
    riff_chunk_size = len(data) - 8
    quotient = riff_chunk_size

    binarray = list()
    for _ in range(4):
        quotient, remainder = divmod(quotient, 256)  # every 8 bits
        binarray.append(remainder)
    riff = data[:4] + bytes(binarray) + data[8:]
    return riff
