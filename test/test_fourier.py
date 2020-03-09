import unittest

import numpy as np

import spyctrum.audio.fourier as fourier

TEST_ARRAY = np.array([
    [0, 0],  # 0.0s
    [1, 1],  # 0.5s
    [2, 2],  # 1.0s
    [3, 3],  # 1.5s
    [4, 4],  # 2.0s
    [5, 5],  # 2.5s
    [6, 6]]) # 3.0s
TEST_SAMPLE_RATE = 2 # 2 per second
TEST_TIMESTAMP = 1.5

class FourierTests(unittest.TestCase):
    def confirm_result(self, chunk, expected):
        if isinstance(chunk, np.ndarray):
            self.assertEqual(chunk.shape[0], len(expected))
        else:
            self.assertEqual(len(chunk), len(expected))

        for i in range(len(expected)):
            self.assertEqual(chunk[i][0], expected[i])

    def get_chunk(self, length, alignment):
        return fourier.get_chunk(TEST_ARRAY,
                                 TEST_TIMESTAMP,
                                 TEST_SAMPLE_RATE,
                                 length,
                                 alignment)

    def get_odd_chunk(self, alignment):
        return self.get_chunk(3, alignment)

    def get_even_chunk(self, alignment):
        return self.get_chunk(4, alignment)
            
    def test_get_chunk_central(self):
        odd = self.get_odd_chunk(fourier.ALIGN_CENTRAL)
        self.confirm_result(odd, [2, 3, 4])

        even = self.get_even_chunk(fourier.ALIGN_CENTRAL)
        self.confirm_result(even, [1, 2, 3, 4])

        overflow = self.get_chunk(8, fourier.ALIGN_CENTRAL)
        self.confirm_result(overflow, [0, 1, 2, 3, 4, 5, 6])

    def test_get_chunk_start(self):
        odd = self.get_odd_chunk(fourier.ALIGN_START)
        self.confirm_result(odd, [3, 4, 5])

        even = self.get_even_chunk(fourier.ALIGN_START)
        self.confirm_result(even, [3, 4, 5, 6])

        overflow = self.get_chunk(5, fourier.ALIGN_START)
        self.confirm_result(overflow, [3, 4, 5, 6])

    def test_get_chunk_end(self):
        odd = self.get_odd_chunk(fourier.ALIGN_END)
        self.confirm_result(odd, [1, 2, 3])

        even = self.get_even_chunk(fourier.ALIGN_END)
        self.confirm_result(even, [0, 1, 2, 3])

        overflow = self.get_chunk(5, fourier.ALIGN_END)
        self.confirm_result(overflow, [0, 1, 2, 3])
