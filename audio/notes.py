import math
import sys

_LOG2_AVAILABLE = False
if sys.version_info.major >= 3 and sys.version_info.minor >= 3:
    _LOG2_AVAILABLE = True

# define frequency of A4 to determine other notes
A4 = 440

LETTER_TABLE = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")

# exponential term
A = 2**(1 / 12)

def note_to_semitone_diff(note: str) -> float:
    """Returns the number of semitones between the input note and A4

# Args:
 - note: string, name of the note (e.g. "A4", "C#4"). Sharps "#"
   should be put _before_ the number. Flats are not supported.

# Returns:
 - diff: float, number of semitones between the note and A4
"""
    letter = note[0].upper()
    sharp = note[1] == "#"
    if sharp:
        if letter in ("B", "E"):
            raise ValueError(letter + "# is not a valid note")
        letter += "#"
        number = float(note[2:])
    else:
        number = float(note[1:])

    diff = 12 * (number - 4) + LETTER_TABLE.index(letter) - 9
    return diff

def semitone_diff_to_frequency(n: float) -> float:
    """Converts a difference in semitones between your target note
and A4 to a frequency

# Args:
 - n: float, number of semitones between target note and A4.
   Does not have to an integer!

# Returns:
 - frequency: float, frequency of the note
"""
    return A4 * A**n

def note_to_frequency(note: str) -> float:
    """Takes an input note name and converts it to its frequency

# Args:
 - note: string, name of the note (e.g. "A4")

# Returns:
 - frequency: float, frequency of the note
"""
    n = note_to_semitone_diff(note)
    return semitone_diff_to_frequency(n)

def frequency_to_semitone_diff(f: float) -> float:
    """Takes an input frequency and converts it to a semitone difference
from A4

# Args:
 - f: float, frequency of the note

# Returns:
 - diff: float, difference in semitones from A4
"""
    if _LOG2_AVAILABLE:
        return 12 * math.log2(f / A4)
    return 12 * math.log(f / A4, 2)

def semitone_diff_to_note(diff: float) -> str:
    """Takes an input semitone difference from A4 and converts it to the
nearest note

# Args:
 - diff: float, difference in semitones from A4

# Returns:
 - note: string, name of the nearest note

    """
    number, letter = divmod(round(diff), 12)
    number += 4
    letter = (letter + 9) % 12
    if letter < 9:
        # if the letter is C-G we need to go up an octave
        number += 1
    letter = LETTER_TABLE[letter]
    return letter + str(number)

def frequency_to_note(f: float) -> float:
    """Takes an input frequency and converts it to the nearest note name

# Args:
 - f: float, frequency of the note

# Returns:
 - note: string, name of the nearest note
"""
    diff = frequency_to_semitone_diff(f)
    return semitone_diff_to_note(diff)
