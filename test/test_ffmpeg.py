import unittest
import subprocess

import spyctrum.audio.ffmpeg

class FFMPEGTests(unittest.TestCase):
    def test_call_normal(self):
        p = spyctrum.audio.ffmpeg.call(["-h"])
        self.assertTrue(isinstance(p, subprocess.Popen))

    def test_call_err(self):
        with self.assertRaises(TypeError):
            spyctrum.audio.ffmpeg.call("test")
