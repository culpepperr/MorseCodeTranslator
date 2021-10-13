# Morse code translator
# This program translates dots and dashes to a message. Only one way currently.
# Can use 'dot' or '.' and 'dash' or '-' 
# examples "... --- ..." or "dotdotdot dashdashdash dotdotdot"
import re
alpha=False
morseMessageTrans = ""

#pull in string input
morseMessage = input("Enter your morse code message - separate words with spaces!-: ")

# change to all lower case to prevent errors
morseMessage = morseMessage.lower()

morseCodeDict = {
  "A" : ".-", "B" : "-...", "C" : "-.-.",  "D" : "-..",  "E" : ".",  "F" : "..-.",  "G" : "--.",
  "H" : "....",  "I" : "..",  "J" : ".---",  "K" : "-.-",  "L" : ".-..",  "M" : "--",  "N" : "-.",
  "O" : "---",  "P" : ".--.",  "Q" : "--.-",  "R" : ".-.",  "S" : "...",  "T" : "-",  "U" : "..-",
  "V" : "...-",  "W" : ".--",  "X" : "-..-",  "Y" : "-.--", "Z" : "--..",

  "1": ".----", "2": "..---","3": "...--","4": "....-","5": ".....",
  "6": "-....","7": "--...","8": "---..","9": "----.","0": "-----",
  " ": " "
  
}

print(morseMessage)

#for word in morseMessage:
  #list.append(word)
listMorse = re.findall("[a-z]",morseMessage)
print("pass")
if len(listMorse) > 0:
  alpha = True
else:
  alpha = False

morseMessageAlpha = ""
if alpha == True:
  print("pass2")
  morseMessageAlpha = re.sub("dot", ".", morseMessage)
  morseMessageAlpha = re.sub("dash", "-", morseMessageAlpha)
  print(morseMessageAlpha)


if len(morseMessageAlpha) > 0:
  morseMessage = morseMessageAlpha
for word in morseMessage.split():
  for key,value in morseCodeDict.items():
    if word == value:
      morseMessageTrans = morseMessageTrans + key


print(morseMessageTrans)
  

