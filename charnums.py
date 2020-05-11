ersatz = {
    "ä": "ae",
    "ö": "oe",
    "ü": "ue",
    "ß": "ss",
    "1": "eins",
    "2": "zwei",
    "3": "drei",
    "4": "vier",
    "5": "fuenf",
    "6": "sechs",
    "7": "sieben",
    "8": "acht",
    "9": "neun",
    "0": "null",
    "°": "grad",
    ".": "punkt",
    "'": "minuten",
}


def _convert(input):
    """Bereite `input` für `charnums` vor."""
    ergebnis = ""
    input = input.lower()

    for x in input:
        if x.isspace():
            continue
        elif x.isascii() and x.isalpha():
            ergebnis += x
        elif x in ersatz:
            ergebnis += ersatz[x]
        else:
            raise ValueError(f"Don't know how to convert {x!r}")
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
    print('To be encoded string:')
    print(_convert(args.string))
    print('Encoded string:')
    print(charnums(args.string))
