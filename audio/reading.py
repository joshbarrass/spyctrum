import os
from io import BytesIO
import tempfile, shutil

from scipy.io import wavfile as _wavfile

from audio.ffmpeg import call as _call
from audio.fixes import fix_RIFF_chunk_sizes

def memread(fp: str):
    """reads an audio file into a numpy array without storing it as a
temporary file

Returns a tuple containing the sample rate in Hz followed by the audio
data

    """
    fp = os.path.abspath(fp)
    p = _call(["-i", fp, "-vn", "-f", "wav",
               "-acodec", "pcm_s16le", "-ac", "2", "-"])
    # read data from process and fix
    data, _ = p.communicate()
    fixed = fix_RIFF_chunk_sizes(data)

    # put raw data into buffer
    buf = BytesIO(fixed)
    return _wavfile.read(buf)

def tempread(fp: str):
    """reads an audio file into a numpy array via a temp file

Returns a tuple containing the sample rate in Hz followed by the audio
data

    """
    fp = os.path.abspath(fp)

    # generate a temp dir to store the file
    tempdir = tempfile.mkdtemp(suffix="spyctrum")
    temppath = os.path.join(tempdir, "temp.wav")

    p = _call(["-i", fp, "-vn", "-f", "wav",
           "-acodec", "pcm_s16le", "-ac", "2", temppath])
    p.wait()

    # read the file
    to_return = _wavfile.read(temppath)
    

    # delete the temp dir
    shutil.rmtree(tempdir)

    return to_return
