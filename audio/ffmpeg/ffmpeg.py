import subprocess
import sys

class FFmpegException(Exception):
    pass

def call(cmd):
    """Calls ffmpeg and returns the subprocess

cmd is the arguments to ffmpeg -- this should not include "ffmpeg" at
the start. Should be a list.

    """
    if not isinstance(cmd, list):
        raise TypeError("cmd must be of type list")
    p = subprocess.Popen(["ffmpeg"] + cmd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         )
    return p
    
# check ffmpeg is installed
_H, _ERRTEXT = call(["-h"]).communicate()
if _H == "":
    raise FFmpegException("ffmpeg not detected")
print(_ERRTEXT.decode("utf-8"), file=sys.stderr)
