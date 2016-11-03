#  File: TestCipher.py
#  Description: This program creates a substitution cipher.
#  Student Name: Minal Kalas
#  Student UT EID: mjk863
#  Course Name: CS 313E
#  Unique Number: 50965
#  Date Created: 03/30/16
#  Date Last Modified: 03/31/16

plain_text = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
cipher_text = [ 'q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p' ]

def substitution_encode (strng):
  txt = ""
  strng = strng.lower()

  # Find the input text's cipher counterpart and add it to the new string to be outputed
  for i in range(0, len(strng)):
    if (strng[i].isalpha() == False):
      txt = txt + strng[i]
    else:
      txt = txt + cipher_text[plain_text.index(strng[i])]
  return txt

def substitution_decode (strng):
  txt = ""
  strng = strng.lower()

  # Find the input text's cipher counterpart and add it to the new string to be outputed
  for i in range(0, len(strng)):
    if (strng[i].isalpha() == False):
      txt = txt + strng[i]
    else:
      txt = txt + plain_text[cipher_text.index(strng[i])]
  return txt

def vigenere_encode (strng, passwd):
  encripted = ""
  passwd = ""
  position = 0
  strng = strng.lower()

  # Loop through the text to be encoded and add the appropriate letter from the pass phrase
  for i in range (0, len(strng)):
    # If the character in the normal text is not a character, just add it to the pass phrase
    if (strng[i] == " "):
      passwd = passwd + " "
      position = position
    elif (strng[i].isalpha() == False):
      passwd = passwd + strng[i]
      position = position
    else:
      passwd = passwd + passwd[position]
      position = (position + 1) % len(passwd)

  # Loop through running the algorithm for each letter to come up with the encoded letter and add it to the text to be outputted
  for i in range(0, len(strng)):
    if (strng[i] == " "):
      encripted = encripted + " "
    elif (strng[i].isalpha() == False):
      encripted = encripted + strng[i]
    else:
      norm_letter = ord(strng[i]) - 97
      pass_letter = ord(passwd[i]) - 97
      letter = chr(((norm_letter + pass_letter) % 26) + 97)
      encripted = encripted + letter
  return (encripted)

def vigenere_decode (strng, passwd):
  decripted = ""
  passwd = ""
  position = 0
  strng = strng.lower()
  
  # Loop through the text to be decoded and add the appropriate letter from the pass phrase
  for i in range (0, len(strng)):
    # If the character in the normal text is not a character, just add it to the pass phrase
    if (strng[i] == " "):
      passwd = passwd + " "
      position = position
    elif (strng[i].isalpha() == False):
      passwd = passwd + strng[i]
      position = position
    else:
      passwd = passwd + passwd[position]
      position = (position + 1) % len(passwd)
  # Loop through running the algorithm for each letter to come up with the encoded letter and add it to the text to be outputted
  for i in range(0, len(strng)):
    if (strng[i] == " "):
      decripted = decripted + " "
    elif (strng[i].isalpha() == False):
      decripted = decripted + strng[i]
    else:
      norm_letter = ord(strng[i]) - 97
      pass_letter = ord(passwd[i]) - 97
      letter = chr(((norm_letter - pass_letter) % 26) + 97)
      decripted = decripted + letter
  return (decripted)

def main():
  # open file for reading
  in_file = open ("./cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()

  # encode using substitution cipher
  encoded_str = substitution_encode (line)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()

  # decode using substitution cipher
  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # close file
  in_file.close()

main()