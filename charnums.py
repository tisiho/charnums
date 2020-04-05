def _convert(input):
    """Bereite `input` für `charnums` vor."""
    no_space = ''
    input = input.lower()
    
    for x in input:
        if not x.isspace():
            no_space += x
    return no_space

def charnums(string):
    """Konvertiere String in Folge von Buchstabenpoitinnen."""
    ergebnis = ""
    for c in _convert(string):
        zw = str(ord(c) - 96)
        ergebnis += zw
    return ergebnis
