morseChart={'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ' ':'/'} # 7 units space between words (1 included per .wav sample, 2 for letter, +4 extra for space = 7)
inv_chart = {a: b for b, a in morseChart.items()}

def morseDecode(message):
    words = message.split("/")
    for word in words:
        letters = word.split(",")
    mc = ""
    for word in words:
        for letter in letters:
            mc += inv_chart[letter]
        mc += " "
    print("Result:"+mc)

print("Morse Decoder")
while True:
    print("Enter morse (.-,-...,-.-./.-,-...,-.-.)")
    userMessage = input(":")
    print("Decoding...")
    morseDecode(userMessage)
    print("Done. (CTRL-C to exit)")
    

