def _convert(input):
    """Bereite `input` für `charnums` vor."""
    no_space = ''
    ergebnis = ""
    input = input.lower()

    for x in input:
        if not x.isspace():
            no_space += x

    ergebnis = no_space.replace("ä", "ae")
    ergebnis = ergebnis.replace("ö", "oe")
    ergebnis = ergebnis.replace("ü", "ue")
    ergebnis = ergebnis.replace("ß", "ss")
    ergebnis = ergebnis.replace("1", "eins")
    ergebnis = ergebnis.replace("2", "zwei")
    ergebnis = ergebnis.replace("3", "drei")
    ergebnis = ergebnis.replace("4", "vier")
    ergebnis = ergebnis.replace("5", "fuenf")
    ergebnis = ergebnis.replace("6", "sechs")
    ergebnis = ergebnis.replace("7", "sieben")
    ergebnis = ergebnis.replace("8", "acht")
    ergebnis = ergebnis.replace("9", "neun")
    ergebnis = ergebnis.replace("0", "null")
    ergebnis = ergebnis.replace("°", "grad")
    ergebnis = ergebnis.replace(".", "punkt")
    ergebnis = ergebnis.replace("'", "minuten")
    return ergebnis


def charnums(string):
    """Konvertiere String in Folge von Buchstabenpositionen."""
    ergebnis = ""
    for c in _convert(string):
        zw = str(ord(c) - 96)
        ergebnis += zw
    return ergebnis


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Convert string in list of positions in alphabet.')
    parser.add_argument(
        'string', type=str, help='the string to be converted')

    args = parser.parse_args()
    print(charnums(args.string))
