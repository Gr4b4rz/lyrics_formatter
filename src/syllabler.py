from typing import Optional

VOWELS = ["a", "ą", "ę", "e", "i", "o", "u", "ó", "y", "A", "Ą", "Ę", "E", "I", "O", "U", "Ó", "Y"]
CONSONANTS = ["b", "c", "ć", "d", "f", "g", "h", "j", "k", "l", "ł", "m", "n", "ń", "p", "r", "s",
              "ś", "t", "w", "z", "ź", "ż", "B", "C", "Ć", "D", "F", "G", "H", "J", "K", "L", "Ł",
              "M", "N", "Ń", "P", "R", "S", "Ś", "T", "W", "Z", "Ź", "Ż"]
SOFTENING_VOWEL = "i"
SOFTENABLE_CONSONANTS = ["b", "c", "d", "f", "g", "h",
                         "k", "l", "m", "n", "p", "r", "s", "t", "w", "z"]
DIGRAMS = ["ch", "cz", "dz", "dź", "dż", "rz", "sz"]


def is_vowel(char: str, nex_char: Optional[str]) -> bool:
    """
    Check if given character is a vowel.
    """
    if char not in VOWELS:
        return False

    if char != SOFTENING_VOWEL:
        return True

    return nex_char not in VOWELS


def split_to_syllables(word: str) -> list[str]:
    """
    Split given Polish word to syllables using simplified rules.
    """
    syllables = []
    vowels = [(pos, char) for pos, char in enumerate(word) if is_vowel(char, word[pos+1]
              if pos + 1 < len(word) else None)]
    next_syllable_start = 0
    for vowel_idx, (pos, _vowel) in enumerate(vowels):
        next_vowel_pos = vowels[vowel_idx+1][0] if vowel_idx + 1 < len(vowels) else None
        # Its last vowel, create last syllable and break
        if next_vowel_pos is None:
            syllables.append("".join(list(word)[next_syllable_start:]))
            break
        # If there are at least 2 characters between vowels,
        # some of them might belong to this syllable
        if next_vowel_pos - pos >= 2:
            # Digrams and softening vowel are handled specially. They make next syllable has
            # two characters before the vowel instead of one.
            if (word[next_vowel_pos-1] == SOFTENING_VOWEL or
                    word[next_vowel_pos - 2] + word[next_vowel_pos-1] in DIGRAMS):
                syllables.append("".join(list(word)[next_syllable_start:next_vowel_pos-2]))
                next_syllable_start = next_vowel_pos-2
            # Next syllable should have one character before the vowel
            else:
                syllables.append("".join(list(word)[next_syllable_start:next_vowel_pos-1]))
                next_syllable_start = next_vowel_pos-1
        # Vowels next to each other, like "aeroplan"
        elif next_vowel_pos - pos == 1:
            syllables.append("".join(list(word)[next_syllable_start:next_vowel_pos]))
            next_syllable_start = next_vowel_pos

    return syllables
