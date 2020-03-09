# define frequency of A4 to determine other notes
A4 = 440

LETTER_TABLE = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#" "B")

# exponential term
A = 2**(1/12)

def semitone_diff(note):
    """Returns the number of semitones between the input note and A4

# Args:
 - note: string, name of the note (e.g. "A4", "C#4"). Sharps "#" should be put _before_ the number. Flats are not supported.

# Returns:
 - diff: float, number of semitones between the note and A4
"""
    letter = note[0].upper()
    sharp = note[1] == "#"
    if sharp:
        if letter == "B" or letter == "E":
            raise ValueError(letter+"# is not a valid note")
        letter += "#"
        number = float(note[2:])
    else:
        number = float(note[1:])

    diff = 12 * (number-4) + LETTER_TABLE.index(letter) - 9
    return diff

def note_to_frequency(note):
    """Takes an input note name and converts it to its frequency

# Args:
 - note: string, name of the note (e.g. "A4")

# Returns:
 - frequency: float, frequency of the note
"""
    # find the number of semitones between this note and A4
    n = semitone_diff(note)

    return A4 * A**n
