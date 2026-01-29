# Text to Morse Code

dict_morse_code = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----"
}
text = str(input("Text to be converted into Morse Code: ").upper())
morse_list = []
unknown_char = []
for every_letter in text:
    if every_letter == " ":
        morse_list.append("/")
    elif every_letter in dict_morse_code:
        letter_morse = dict_morse_code[every_letter]
        morse_list.append(letter_morse)
    else:
        unknown_char.append(every_letter)
        morse_list.append("?")


morse_code=" ".join(morse_list)
if unknown_char:
    unknown_char = "".join(unknown_char)
    print(f" Found unknown characters: {unknown_char} \n unknown characters will be replaced with '?'")
print(f" Text translate from: \n {text} \n in morse code is \n {morse_code} ")