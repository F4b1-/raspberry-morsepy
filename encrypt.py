import morsing
import RPi.GPIO as GPIO
import sys






MorseAlph =  {'a': "01", "b": "1000", "c": "101", "d": "100",  "e": "0", "f": "0010",  "g": "110",  "h": "0000",
               "i": "00", "j": "0111", "k": "101", "l": "0100", "m": "11", "n": "10", "o": "111", "p": "0110",
               "q": "1101", "r": "010", "s": "000", "t": "1",
                "u": "001", "v": "0001", "w": "011", "x": "1001", "y": "1011",
                "z": "1100", "1":"00001","2":"00011","3":"00111","4":"01111",
                "5":"11111","6":"011111","7":"00111","8":"00011","9":"00001"}

output = ''


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


while(True):
       
    
        new_input = input('please type in your message to get the morse code : ')
        if new_input == "/close":
                GPIO.cleanup()
                sys.exit()

        for letter in new_input:
                if letter != ' ':
                        output = output + MorseAlph[letter]

        print ('Morsing: ' + output)
        morsing.morse(output)
        output = ''
       






