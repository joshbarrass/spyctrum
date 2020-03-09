import subprocess
import sys

FFMPEG_INSTALLED = False

class FFmpegException(Exception):
    pass

def call(cmd):
    """Calls ffmpeg with some useful defaults and returns the
subprocess. The ffmpeg command is already entered into the arguments
and both stdout and stderr are piped so they can be read directly in
Python.

## Args:
- cmd: arguments to ffmpeg. This should not include "ffmpeg" at
    the start. Should be a list.

## Returns:
- p: ffmpeg process Popen. Will not run by itself; you
    must call a function such as p.wait() or p.communicate() for the
    process to finish.

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
    #raise FFmpegException("ffmpeg not detected")
    print("ffmpeg was not detected. ffmpeg functions will be disabled.", file=sys.stderr)
else:
    print(_ERRTEXT.decode("utf-8"), file=sys.stderr)
    FFMPEG_INSTALLED = True
