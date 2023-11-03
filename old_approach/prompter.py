import argparse
import math

CHARS_IN_LINE = 24
LINES_IN_FRAME = 8
FRAME_SIZE = CHARS_IN_LINE * (LINES_IN_FRAME + 2)  # 8 lines with text and 2 empty ones
FRAMES_IN_SONG = 17  # 15 with text, 2 empty + title
SONG_PADDING_LEN = 16  # 16 characters, probably for memory alignment
SONG_MAX_LEN = FRAME_SIZE * FRAMES_IN_SONG + SONG_PADDING_LEN  # 2^12 == 4096
CATEGORY_MAX_LEN = SONG_MAX_LEN * 64  # 2^18 == 262144
TRALING_DOTS_LEN = 128  # 2^7


# TODO: Support new categories
def parse_args():
    "Parse arguments passed by cli"
    parser = argparse.ArgumentParser(prog="Shield Filler",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("category", action="store", type=str, help="Category name")
    parser.add_argument("input_file", action="store", type=str, help="Input filename")
    parser.add_argument("title", action="store", type=str, help="Song title")

    args = parser.parse_args()
    return args


def read_frames(input_file) -> list[str]:
    with open(input_file, mode="r") as f:
        data = f.read().splitlines()
    frames = []
    frame = ""
    for line in data:
        if line:
            if frame:
                frame += " "
            frame += line
        else:
            frames.append(frame)
            frame = ""

    return frames


def format_frame_thriftily(frame: str) -> str:
    lines: list[str] = []
    words = frame.split()
    line = ""
    for word in words:
        if line and len(line) < CHARS_IN_LINE:
            line += " "
        if len(line) + len(word) + 1 <= CHARS_IN_LINE:
            if line:
                line += " "
            line += word
        elif 24 - len(line) > 4:
            add_part_of_word()
        else:
            lines.append(line)
            line = word

    if line:
        lines.append(line)

    assert (len(lines) <= LINES_IN_FRAME)
    formatted_frame = "".join([line.ljust(24, " ") for line in lines])
    for _ in range(LINES_IN_FRAME + 2 - len(lines)):
        formatted_frame += " " * CHARS_IN_LINE
    return formatted_frame


def format_frame(frame: str) -> str:
    lines: list[str] = []
    words = frame.split()
    line = ""
    for word in words:
        if line and len(line) < CHARS_IN_LINE:
            line += " "
        if len(line) + len(word) <= CHARS_IN_LINE:
            line += word
        else:
            lines.append(line)
            line = word

    if line:
        lines.append(line)

    print(lines)
    assert (len(lines) <= LINES_IN_FRAME)
    formatted_frame = "".join([line.ljust(24, " ") for line in lines])
    for _ in range(LINES_IN_FRAME + 2 - len(lines)):
        formatted_frame += " " * CHARS_IN_LINE
    return formatted_frame


def main():
    with open("VISOR.DAT", mode="r", encoding="cp1250") as f:
        data = f.read()
    pos = data.find("ADWENT")
    categories = [(data[pos + CATEGORY_MAX_LEN * x: pos + CATEGORY_MAX_LEN * x + 26].strip())
                  for x in range(15)]
    print("Kategorie")
    print("=========")
    print(categories)
    print()
    arguments = parse_args()
    assert arguments
    assert arguments.category in categories

    category_idx = categories.index(arguments.category)
    # TODO: check category limits
    position_to_add = data.find("˙" * SONG_MAX_LEN, CATEGORY_MAX_LEN * category_idx)
    position_to_add = math.ceil(position_to_add / SONG_MAX_LEN) * SONG_MAX_LEN

    frames = read_frames(arguments.input_file)
    song = ""
    for frame in frames:
        song += format_frame(frame)

    assert len(song) == CHARS_IN_LINE * LINES_IN_FRAME * len(frames)
    for _ in range(FRAMES_IN_SONG - len(frames) - 1):
        song += " " * CHARS_IN_LINE * LINES_IN_FRAME
    song += arguments.title.ljust(CHARS_IN_LINE * LINES_IN_FRAME + SONG_PADDING_LEN -
                                  TRALING_DOTS_LEN, " ")
    song += "˙" * TRALING_DOTS_LEN

    assert len(song) == SONG_MAX_LEN

    data = data[:position_to_add] + song + data[position_to_add + SONG_MAX_LEN:]
    print("Dodany utwór")
    print("============")
    print(data[position_to_add - SONG_MAX_LEN:position_to_add + SONG_MAX_LEN + 100])

    #  with open("prompter.DAT", mode="w", encoding="cp1250") as f:
    #  f.write(data)


if __name__ == '__main__':
    main()
