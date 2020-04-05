def _convert(input):
    """Bereite `input` für `charnums` vor."""


def charnums(string):
    """Konvertiere String in Folge von Buchstabenpoitinnen."""
    ergebnis = ""
    for c in string:
        zw = str(ord(c) - 96)
        ergebnis += zw
    return ergebnis
