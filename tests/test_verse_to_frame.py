from src.verse_to_frame import verse_to_frame, verse_to_frame_thriftily, get_word_parts


def test_word_splitting():
    "Test spltting word on the line break"
    assert get_word_parts("ciemność", 5) == ("ciem-", "ność")
    assert get_word_parts("wszystko", 5) == ("", "wszystko")
    assert get_word_parts("sióstr", 7) == ("sióstr", "")
    assert get_word_parts("sióstr", 5) == ("", "sióstr")
    assert get_word_parts("wiedźmy", 5) == ("", "wiedźmy")
    assert get_word_parts("drożdżówka", 6) == ("droż-", "dżówka")
    assert get_word_parts("alias", 4) == ("a-", "lias")
    assert get_word_parts("aerodynamiczny", 5) == ("aero-", "dynamiczny")


def test_verse_to_frame_conversion():
    "Test normal and thrifty conversion"
    verse = ['1. Będę błogosławił Pana po wieczne czasy,',
             'Jego chwała będzie zawsze na moich ustach.',
             'Dusza moja chlubi się Panem,',
             'niech słyszą to pokorni i niech się weselą.']
    frame = verse_to_frame(verse)
    assert frame == ['1. Będę błogosławił Pana',
                     'po wieczne czasy, Jego  ',
                     'chwała będzie zawsze na ',
                     'moich ustach. Dusza moja',
                     'chlubi się Panem, niech ',
                     'słyszą to pokorni i     ',
                     'niech się weselą.       ',
                     '                        ']

    verse_long = ['4. Anioł Pana otacza szańcem bogobojnych,',
                  'aby ocalić tych, którzy w Niego wierzą,',
                  'skosztujcie i zobaczcie, jak Pan jest dobry,',
                  'szczęśliwy człowiek, który się do Niego ucieka.']
    frame = verse_to_frame(verse_long)
    assert frame is None

    frame = verse_to_frame_thriftily(verse_long)
    assert frame == ['4. Anioł Pana otacza    ',
                     'szańcem bogobojnych, aby',
                     'ocalić tych, którzy w   ',
                     'Niego wierzą, skosztuj- ',
                     'cie i zobaczcie, jak Pan',
                     'jest dobry, szczęśliwy  ',
                     'człowiek, który się do  ',
                     'Niego ucieka.           ']
