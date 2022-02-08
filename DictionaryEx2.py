def main():
    codes = {
        "a": "#",
        "b": "%",
        "c": "^",
        "d": "&",
        "e": "*",
        "f": ")",
        "g": "-",
        "h": "(",
        "i": "?",
        "j": "<",
        "k": 1,
        "l": 3,
        "m": "}",
        "n": "[",
        "o": "{",
        "p": 13,
        "q": "`",
        "r": "@",
        "s": 61,
        "t": 11,
        "u": 15,
        "v": 17,
        "w": 7,
        "x": 9,
        "y": 22,
        "z": 55,
        "A": ">",
        "B": 29,
        "C": 5,
        "D": 53,
        "E": "+",
        "F": "=",
        "G": 13,
        "H": "_",
        "I": "!",
        "J": 19,
        "K": 21,
        "L": 23,
        "M": 25,
        "N": 27,
        "O": "]",
        "P": 31,
        "Q": 33,
        "R": 35,
        "S": 37,
        "T": 39,
        "U": 41,
        "V": 43,
        "W": 45,
        "X": 47,
        "Y": 49,
        "Z": 51,
    }

    txt_encrypted = ""
    encrypt_infile = open("info_security.txt", "r")
    for line in encrypt_infile:
        for ch in line:
            if ch in codes:
                txt_encrypted += str(codes[ch])
            else:
                txt_encrypted += ch  # to solve for unaccounted for characters in other potential texts

    encrypt_infile.close()

    encrypt_outfile = open("info_encrypted.txt", "w")
    encrypt_outfile.write(txt_encrypted)
    encrypt_outfile.close()


main()
