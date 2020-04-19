def _convert(input):
    """Bereite `input` für `charnums` vor."""
    no_space = ''
    no_ÄÖÜ = ""
    input = input.lower()

    for x in input:
        if not x.isspace():
            no_space += x

    no_ÄÖÜ = no_space.replace("ä", "ae")
    no_ÄÖÜ = no_ÄÖÜ.replace("ö", "oe")
    no_ÄÖÜ = no_ÄÖÜ.replace("ü", "ue")
    no_ÄÖÜ = no_ÄÖÜ.replace("ß", "ss")
    return no_ÄÖÜ


def charnums(string):
    """Konvertiere String in Folge von Buchstabenpoitinnen."""
    ergebnis = ""
    for c in _convert(string):
        zw = str(ord(c) - 96)
        ergebnis += zw
    return ergebnis
