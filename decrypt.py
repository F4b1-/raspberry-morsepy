new_input = raw_input('please type in your morsecode to get the message : ' ) + ' '
new_input = new_input.replace('-', '1').replace('.', '0')

MorseAlph =  {"a": "01", "b": "1000", "c": "1010", "d": "100",  "e": "0", "f": "0010",  "g": "110",  "h": "0000",
               "i": "00", "j": "0111", "k": "101", "l": "0100", "m": "11", "n": "10", "o": "111", "p": "0110",
               "q": "1101", "r": "010", "s": "000", "t": "1",
                "u": "001", "v": "0001", "w": "011", "x": "1001", "y": "1011",
                "z": "1100", "1":"00001","2":"00011","3":"00111","4":"01111",
                "5":"11111","6":"011111","7":"00111","8":"00011","9":"00001", "": ""}

MorseAlphRev = dict(zip(MorseAlph.values(),MorseAlph.keys()))

output = ''
letter = ''

for bit in new_input:
    if bit == '1' or bit == '0':
        letter = letter + bit
    elif (letter == ''):
        output = output + ' '
    else:
        output = output + MorseAlphRev[letter]
		letter = ''

print output
