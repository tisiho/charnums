from charnums import charnums

def test_charnum_1():
    """Konvertiert String aus kleinen Buchstaben"""
    assert charnums("hallo") == "81121215"
