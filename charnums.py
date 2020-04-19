ersatz = {
    '1': 'eins',
    '2': 'zwei',
    '3': 'drei',
    '4': 'vier',
    '5': 'fuenf',
    '6': 'sechs',
    '7': 'sieben',
    '8': 'acht',
    '9': 'neun',
    '0': 'null',
    '°': 'grad',
    '.': 'punkt',
    "'": 'minuten',
}


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
