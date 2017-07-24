# Secret Messages program for Treehouse
#
# ** encrypts and decrypts messages **
#
# Author: Bryce Swarm

import string

from Secret_messages.ciphers import Cipher


class Atbash(Cipher):
    """Encrypts and Decrypts messages using the Atbash cipher,
       takes one input of 'message' to modify"""

    def __init__(self):
        # Creating alphabet list and a reversed alphabet list
        self.alphabet = list(string.ascii_uppercase)
        self.reversed_alphabet = list(string.ascii_uppercase)[::-1]

    # Encrypts message using both alphabets
    def encrypt(self, text):
        """Encrypts the user message by matching the index of the entered
           letter to the encrypted alphabet index, then matching back to the
           alphabet to obtain encrypted letter.

           Example:
           index of 'A' is 0 on standard alphabet
           encrypted version of 'A' is 'Z'
           as 'Z' is index 0 on encrypted alphabet"""
        output = []

        for letter in text:
            try:
                index = self.alphabet.index(letter)
            except ValueError:
                output.append(letter)
            else:
                output.append(self.reversed_alphabet[index])
        return ''.join(output)

    # Decrypts message using both alphabets
    def decrypt(self, text):
        """Encrypts the user message by matching the index of the entered
           letter to the encrypted alphabet index, then matching back to the
           alphabet to obtain encrypted letter.

           Example:
           index of 'Z' is 0 on encrypted alphabet
           decrypted version of 'Z' is 'A'
           as 'A' is index 0 on standard alphabet"""
        output = []

        for letter in text:
            try:
                index = self.reversed_alphabet.index(letter)
            except ValueError:
                output.append(letter)
            else:
                output.append(self.alphabet[index])
        return ''.join(output)