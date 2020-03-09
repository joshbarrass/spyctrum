import unittest
import numpy as np

import spyctrum.audio.notes as notes

C = [16.352, 32.703, 65.406, 130.813, 261.626, 523.251, 1046.502,
     2093.005, 4186.009, 8372.018, 16744.036]
C_FIGS = [5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8]

A_SHARP = 466.164
A_SHARP_FIGS = 6

class NoteTests(unittest.TestCase):
    def test_A4(self):
        self.assertTrue(notes.note_to_frequency("A4"), notes.A4)

    def test_C(self):
        for i in range(len(C)):
            np.testing.assert_approx_equal(
                notes.note_to_frequency("C{i}".format(i=i)),
                C[i],
                C_FIGS[i],
            )

    def test_Asharp4(self):
        np.testing.assert_approx_equal(
            notes.note_to_frequency("A#4"),
            A_SHARP,
            A_SHARP_FIGS,
        )
