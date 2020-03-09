import unittest
import spyctrum.audio.reading as reading
from spyctrum.audio import Audio
import os
import sys
import numpy as np

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE = os.path.join(TEST_DIR, "test.flac")

TEST_RATE = 44100
TEST_SHAPE = (44100, 2)
FIRST_SAMPLE = (0, 0)
LAST_SAMPLE = (-1164, -1164)

class ReadTests(unittest.TestCase):
    def test_memread(self):
        rate, a = reading.memread(TEST_FILE)
        self.assertEqual(rate, TEST_RATE)
        self.assertEqual(a.shape, TEST_SHAPE)
        self.assertEqual(tuple(a[0, :]), FIRST_SAMPLE)
        self.assertEqual(tuple(a[-1, :]), LAST_SAMPLE)

    def test_tempread(self):
        rate, a = reading.tempread(TEST_FILE)
        self.assertEqual(rate, TEST_RATE)
        self.assertEqual(a.shape, TEST_SHAPE)
        self.assertEqual(tuple(a[0, :]), FIRST_SAMPLE)
        self.assertEqual(tuple(a[-1, :]), LAST_SAMPLE)

class ObjTests(unittest.TestCase):
    def setUp(self):
        self.a = Audio(TEST_FILE)

    def tearDown(self):
        self.a = None

    def test_read(self):
        self.assertEqual(self.a.rate, TEST_RATE)
        self.assertEqual(self.a.data.shape, TEST_SHAPE)
        self.assertEqual(tuple(self.a.data[0, :]), FIRST_SAMPLE)
        self.assertEqual(tuple(self.a.data[-1, :]), LAST_SAMPLE)

    def test_fourierFreq(self,):
        self.assertEqual(tuple(self.a.fourierFreq(20)), tuple(np.fft.fftfreq(20, 1/self.a.rate)))
        self.assertEqual(tuple(self.a.fourierFreq(50)), tuple(np.fft.fftfreq(50, 1/self.a.rate)))
