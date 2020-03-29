from charnums import charnums


def test_charnums_0():
    """It returns an empty string for an empty string."""
    assert charnums('') == ''


def test_charnum_1():
    """Konvertiert String aus kleinen Buchstaben"""
    assert charnums("hallo") == "81121215"
