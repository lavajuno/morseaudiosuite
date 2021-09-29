import wave
import struct

# Time in samples (assuming 48000hz sample rate -- best for morse)
# 0.1s: 4800, 0.05s: 2400, etc.
UNIT_TIME = 2400

# Value at which an amplitude is considered ON or OFF. (0-16384) Default value is 12000
AMPLITUDE_LOGIC_THRESHOLD = 12000

# Exact amplitude at which the program recognizes a code transmission has started.
# Should be similar to the amplitude logic threshold, if not the same.
START_DECODE_AMPLITUDE = 12000

# Offset (in samples) to apply to start decoding.
# This is necessary because (ideally) the start listener won't trip until midway up the first wave.
# It shouldn't be necessary to change this unless the frequency of the input code is changed. (Default: 550 Hz)
START_DECODE_OFFSET = -8

MORSE_ENCODE_CHART={'A':'.-', 'B':'-...',
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
                    '0':'-----', ' ':'/'}

MORSE_DECODE_CHART = {a: b for b, a in MORSE_ENCODE_CHART.items()}

# Decode a deviation value to logical ON or OFF
def logicalDecode(deviation):
    if(deviation > AMPLITUDE_LOGIC_THRESHOLD):
        return 1
    else:
        return 0

# Find the average absolute deviation from zero of a chunk. Should be half the amplitude of the wave.
def avgAbsDeviation(chunk):
    totFrames = 0
    for frame in chunk:
        totFrames += abs(frame)
    return totFrames / len(chunk)

# Find the start of the morse code data in a stream using the amplitude
def findStart(chunk):
    iterIndex = 0
    while(abs(chunk[iterIndex]) < START_DECODE_AMPLITUDE):
        iterIndex += 1
    iterIndex += START_DECODE_OFFSET
    if(iterIndex < 0):
        iterIndex = 0
    return iterIndex

# Get raw morse data from a wav file - the heart of the program
def getMorseData(filename):
    with wave.open(filename, "r") as f:
        sampleRate = f.getframerate()
        nFrames = f.getnframes()
        expFrames = []
        chunkDevs = []
        decodedChunks = []
        
        # Unpack the frames of the input .wav file
        for i in range(0, nFrames):
            sFrame = f.readframes(1)
            expFrames.append(struct.unpack("<h", sFrame)[0])

        # Find the start of the morse data
        startSample = findStart(expFrames) 

        # Split wav data into chunks and analyze the avg. abs. deviation of each chunk
        chunkIter = startSample + UNIT_TIME
        while(chunkIter < nFrames - int(UNIT_TIME - 1)): 
            chunk = expFrames[int(chunkIter - UNIT_TIME):int(chunkIter)]
            chunkDevs.append(int(avgAbsDeviation(chunk)))
            chunkIter += UNIT_TIME
            
        # Get logic zeros or ones from average abs. deviation
        for i in chunkDevs:
            decodedChunks.append(logicalDecode(i))
        return decodedChunks
        

# Convert raw morse into human readable dits, dahs, and slashes.
def getHumanReadableMorse(morseData):
    humanMorse = ""
    morseIter = 0
    streak0 = 0
    streak1 = 0
    while(morseIter < len(morseData)): # Iterate over each item and determine if it is the start, end, or part of a character.
        if(morseData[morseIter] == 1):
            if(streak0 > 6):
                humanMorse += "/" # 7 zeroes in a row means a space.
                streak0 = 0
                streak1 = 0
            elif(streak0 > 2): # 3 zeroes in a row means a new character.
                humanMorse += ","
                streak0 = 0
                streak1 = 0
            else:
                streak0 = 0
            streak1 += 1
        else:
            if(streak1 > 2):
                humanMorse += "-" # 3 ones in a row means a dah.
                streak1 = 0
                streak0 = 0
            elif(streak1 > 0):
                humanMorse += "." # 1 one means a dit.
                streak1 = 0
                streak0 = 0
            else:
                streak1 = 0
            streak0 += 1
        morseIter += 1
    return humanMorse

#Decode human readable morse into letters, numbers, and spaces.
def decodeHumanReadableMorse(message):
    words = message.split("/")
    i = 0
    letters = []
    for word in words:
        letters.append(word.split(","))
    mc = ""
    for letter in letters:
        for code in letter:
            try:
                mc += MORSE_DECODE_CHART[code]
            except KeyError as e:
                mc += "?"
        mc += " "
    return(mc)

print("KD2WZZ's WAV to Morse Converter")
while True:
    print("Enter .wav file to decode (example.wav)")
    usrin = input(":")
    print("Analyzing audio...")
    md = getMorseData(usrin)
    hm = getHumanReadableMorse(md)
    mc = decodeHumanReadableMorse(hm)
    print(mc)
    print("Done. (CTRL-C to exit)")
    
