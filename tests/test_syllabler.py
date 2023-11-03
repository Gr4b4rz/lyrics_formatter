from src.syllabler import split_to_syllables


def test_syllables():
    "Check basic word to syllables division"
    assert split_to_syllables("ciemność") == ["ciem", "ność"]
    assert split_to_syllables("wszystko") == ["wszyst", "ko"]
    assert split_to_syllables("sióstr") == ["sióstr"]
    assert split_to_syllables("wiedźmy") == ["wiedź", "my"]
    assert split_to_syllables("drożdżówka") == ["droż", "dżów", "ka"]
    assert split_to_syllables("alias") == ["a", "lias"]
    assert split_to_syllables("aerodynamiczny") == ["a", "e", "ro", "dy", "na", "micz", "ny"]
