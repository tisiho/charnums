from charnums import charnums
from charnums import _convert
import pytest


def test_charnums__charnums__0():
    """It returns an empty string for an empty string."""
    assert charnums('') == ''


def test_charnums__charnums__1():
    """Konvertiert String aus kleinen Buchstaben"""
    assert charnums("hallo") == "81121215"


def test_charnums__charnums__2():
    """Konvertiert String aus Großbuchstaben."""
    assert charnums("HaLLo") == "81121215"


def test_charnums___convert__1():
    """Konvertiert Großbuchstaben in Kleinbuchstaben."""
    assert _convert("HaLLo") == "hallo"


def test_charnums___convert__2():
    """Entfernt Leerzeichen."""
    assert _convert(" H a    LLo  ") == "hallo"


def test_charnums___convert__3():
    """Übersetzt Umlaute in zwei Buchstaben."""
    assert _convert("ÄÖÜßäöü") == "aeoeueßaeoeue"


@pytest.mark.parametrize("input,output", (
    ("1", "eins"),
    ("2", "zwei"),
    ("3", "drei"),
    ("4", "vier"),
    ("5", "fuenf"),
    ("6", "sechs"),
    ("7", "sieben"),
    ("8", "acht"),
    ("9", "neun"),
    ("0", "null"),
))
def test_charnums___convert_4(input, output):
    """Übersetzt Ziffern in Buchstaben."""
    assert _convert(input) == output
