"""
Lyrics formatter.
This program uses input lyrics files to creates files that can be imported to OrionGT controller.

It expects input song to be in format presented below. Verse means here both verse and chorus:
<verse>
<empty line>
<verse>
<empty line>
...
<verse>

Ouput format follows certain strict rules enforced by board size, and OrionGT import API:
- Each line could have maximally 24 characters
- If line has less than 24 characters, fill it with whitespaces
- Each frame could have maximally 8 lines
- If frame has less than 8 lines, fill it with empty lines (with 24 whitespaces each)
- Each song could have maximally 15 frames
- If song has less than 15 frames, fill it with empty frames (with 8 lines of 24 whitespaces each)
- First line is used for a title. It can have maximally 27 characters
- If the title has less than 27 characters, fill it with whitespaces
- Whole file should have 121 lines (title + 15 * 8)
- Every line needs to be ended with '\r\n'
- File should be saved with windows-1250 encoding (cp1250)
- Whole file should have 3149 bytes
- File should be named in XX.TXT pattern e.g. 00.TXT, 01.TXT ...
"""
import argparse
import os
from src.verse_to_frame import (verse_to_frame, verse_to_frame_thriftily, CHARS_IN_LINE,
                                LINES_IN_FRAME)

FRAMES_IN_SONG = 15
LINES_IN_SONG = 1 + FRAMES_IN_SONG * LINES_IN_FRAME  # 1 means title


class VerseTooLongError(Exception):
    "Raised when verse is too long for the OrionGT controller"


class SongTooLongError(Exception):
    "Raised when there are too many verses in a song for the OrionGT controller"


class LyricsFileNotProvidedError(Exception):
    "Raised when input file with lyrics was not provided"


def parse_args():
    "Parse arguments passed by cli"
    parser = argparse.ArgumentParser(prog="Lyrics formatter",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input_file", action="store", type=str, help="Input filename")
    parser.add_argument("title", action="store", type=str, help="Song title")
    parser.add_argument("--output_file", action="store", type=str, help="Input filename")
    parser.add_argument("--check", action="store", type=str, help="Check if song is already "
                        "in SD card. Provide file with controller memory")

    args = parser.parse_args()
    return args


def format_lyrics(lyrics: list[str]) -> list[str]:
    """
    Format song lyrics to the OrionGT format which is described at the very top of this file.
    """
    verses = get_verses(lyrics)
    frames = []
    for verse in verses:
        frame = verse_to_frame(verse)
        if frame:
            frames.append(frame)
            continue
        frame = verse_to_frame_thriftily(verse)
        if not frame:
            raise VerseTooLongError("Too long verse for the OrionGT controller")
        frames.append(frame)

    if len(frames) > FRAMES_IN_SONG:
        raise SongTooLongError("This song is too long - it has more than 15 verses")

    return [line for frame in frames for line in frame]


def get_verses(lyrics) -> list[list[str]]:
    """
    Assuming that verses are separated with an empty line, create verses from list of str lines
    """
    verses: list[list[str]] = []
    verse: list[str] = []
    for line in lyrics:
        if line:
            verse.append(line)
        else:
            verses.append(verse)
            verse = []
    if verse:
        verses.append(verse)

    return verses


def check_if_already_added(data_file: str, title: str) -> bool:
    "Check naively if title is in data file. It doesn't check song lyrics!"
    with open(data_file, mode="r", encoding="cp1250") as file:
        data = file.read().lower()
    return title.lower().strip() in data


def main():
    "Main Lyrics Formatter function"
    arguments = parse_args()
    if arguments.check:
        is_in_memory = check_if_already_added(arguments.check, arguments.title)
        if is_in_memory:
            print("Title has been found in the data file")
        else:
            print("Title has not been found in the data file")
        return is_in_memory

    if not arguments.input_file:
        raise LyricsFileNotProvidedError("Input file with lyrics was not provided")

    with open(arguments.input_file, mode="r", encoding="utf-8") as file:
        lyrics = file.read().splitlines()

    lyrics_lines = format_lyrics(lyrics)
    lyrics_lines = [arguments.title.ljust(27)] + lyrics_lines
    lyrics_lines.extend(["".ljust(CHARS_IN_LINE)] * (LINES_IN_SONG - len(lyrics_lines)))
    output = '\r\n'.join(lyrics_lines) + '\r\n'

    # Magic number of bytes in OrionGT import/export files
    assert len(output) == 3149

    filename = arguments.output_file

    if not filename:
        output_files = [file for file in os.listdir(os.path.dirname(os.path.realpath(__file__))) if
                        file.endswith(".TXT")]
        for num in range(99):
            filename = f"{num:02d}" + ".TXT"
            if filename not in output_files:
                break
    with open(filename, mode="w", encoding="cp1250") as file:
        file.write(output)

    print(f'Converted "{arguments.title}" and saved in {filename}')


if __name__ == '__main__':
    main()
