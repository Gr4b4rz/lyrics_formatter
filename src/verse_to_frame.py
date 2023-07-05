from typing import Optional
from src.syllabler import split_to_syllables

CHARS_IN_LINE = 24
LINES_IN_FRAME = 8


def verse_to_frame(verse: list[str]) -> Optional[list[str]]:
    """
    Try to convert verse in original format to frame-fitting format.
    Try to put as many full words in one line as its possible.
    Frame has maximally 8 lines of 24 characters each. If its impossible to
    fit in this limit, return None.
    Use whitespaces to adjust frame to have excactly 8 lines with exactly 24 characters as it is
    required by OrionGT format.
    """
    frame: list[str] = []
    frame_line = ""
    for line in verse:
        words = line.split()
        for word in words:
            # word fits into the line normally
            if len(frame_line) + len(word) + 1 <= CHARS_IN_LINE:
                if frame_line:
                    frame_line += " "
                frame_line += word
            # No space for a whitespace and word, go to the next line
            else:
                frame.append(frame_line.ljust(CHARS_IN_LINE))
                frame_line = word

    if frame_line:
        frame.append(frame_line.ljust(CHARS_IN_LINE))

    if len(frame) > LINES_IN_FRAME:
        return None
    for _ in range(LINES_IN_FRAME - len(frame)):
        frame.append("".ljust(CHARS_IN_LINE))

    return frame


# TODO: handle dash inside a word, like polsko-angielski
def get_word_parts(word: str, space: int) -> tuple[str, str]:
    """
    Try to get word parts according to the Polish rules of splitting words on line breaks.
    If space for the first word part was not big enough to fit even one syllable, return empty
    string as a first part and full word as a second part.
    """
    syllables = split_to_syllables(word)
    if len(syllables) == 1:
        return (word, "") if len(word) <= space else ("", word)
    first_part = ""
    second_part = word
    for syllable in syllables:
        if len(first_part) + len(syllable) + len("-") <= space:
            first_part += syllable
        else:
            if first_part:
                second_part = second_part.removeprefix(first_part)
                first_part += "-"
            break
    return first_part, second_part


def verse_to_frame_thriftily(verse: list[str]) -> Optional[list[str]]:
    """
    Same as verse_to_frame, but used when verse is too long to fit in a frame limits.
    Thrifitily means here that all gaps longer than 4 whitespaces will be filled by
    word parts. Parts are created according to the Polish rules of dividing words to syllables.

    Code here assumes that one word won't be longer than 24 characters, and its almost True
    """
    frame: list[str] = []
    frame_line = ""
    for line in verse:
        words = line.split()
        for word in words:
            # word fits into the line normally
            if len(frame_line) + len(word) + 1 <= CHARS_IN_LINE:
                if frame_line:
                    frame_line += " "
                frame_line += word
            # word doesn't fit into the line, try to fit its part
            elif CHARS_IN_LINE - len(frame_line) > 4:
                space = CHARS_IN_LINE - len(frame_line) - len(" ")
                first_part, second_part = get_word_parts(word, space)
                # if at least one syllable + "-" fits
                if first_part:
                    frame_line += " "
                    frame_line += first_part
                    frame.append(frame_line.ljust(CHARS_IN_LINE))
                    frame_line = second_part
                # if even one syllable was too long, just don't split this word
                else:
                    frame.append(frame_line.ljust(CHARS_IN_LINE))
                    frame_line = word
            # No space to add a word part, go to the next line
            else:
                frame.append(frame_line.ljust(CHARS_IN_LINE))
                frame_line = word

    if frame_line:
        frame.append(frame_line.ljust(CHARS_IN_LINE))

    if len(frame) > LINES_IN_FRAME:
        return None
    for _ in range(LINES_IN_FRAME - len(frame)):
        frame.append("".ljust(CHARS_IN_LINE))

    return frame
