from charnums import charnums


def test_charnums_0():
    """It returns an empty string for an empty string."""
    assert charnums('') == ''
