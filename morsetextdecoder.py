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
    i = 0
    letters = []
    for word in words:
        letters.append(word.split(","))
    mc = ""
    for letter in letters:
        for code in letter:
            mc += inv_chart[code]
        mc += " "
    print("Result: "+mc)

print("Morse Decoder")
while True:
    print("Enter morse (.-,-...,-.-./.-,-...,-.-.)")
    userMessage = input(":")
    print("Decoding...")
    morseDecode(userMessage)
    print("Done. (CTRL-C to exit)")
    

