# Secret Messages program for Treehouse
#
# ** encrypts and decrypts messages **
#
# Author: Bryce Swarm

import copy
import string

from ciphers import Cipher


class Keyword(Cipher):
    """Encrypts and Decrypts a message using the Keyword cipher.
       Takes an input of a message and a keyword"""

    def __init__(self, keyword = None):
        # asks user for keyword or takes passed in keyword
        if not keyword:
            self.user_keyword = list(input('Please enter a keyword of unique letters'
                                           '\n> ').upper())
        else:
            self.user_keyword = keyword.upper()

        # creates two lists of the english alphabet
        self.alphabet = list(string.ascii_uppercase)
        self.removed_alphabet = copy.copy(self.alphabet)

    # Creates the alphabet, with keyword first followed by alphabet missing letters in the keyword
    def alphabet_removed(self):
        for letter in self.user_keyword:
            if letter in self.removed_alphabet:
                self.removed_alphabet.remove(letter)
        output = (self.user_keyword + self.removed_alphabet)
        return output

    # Encrypts user's message
    def encrypt(self, text):
        """Encrypts the user message by matching the index of the entered
           letter to the encrypted alphabet index, then matching back to the
           alphabet to obtain encrypted letter.

           Example, if keyword == 'KEYWORD':
           index of 'A' is 0 on standard alphabet
           encrypted version of 'A' is 'K'
           as 'K' is index 0 on encrypted alphabet"""
        output = []
        keyword_alphabet = self.alphabet_removed()

        for letter in text:
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                output.append(keyword_alphabet[index])
            else:
                output.append(letter)
        return ''.join(output)

    # Decrypts user's message
    def decrypt(self, text):
        """Decrypts the user message by matching the index of the entered
           letter to the encrypted alphabet index, then matching back to the
           alphabet to obtain decrypted letter.

           Example, if keyword == 'KEYWORD':
           index of 'K' is 0 on encrypted alphabet
           decrypted version of 'K' is 'A'
           as 'A' is index 0 on standard alphabet"""
        output = []
        keyword_alphabet = self.alphabet_removed()

        for letter in text:
            if letter in keyword_alphabet:
                index = keyword_alphabet.index(letter)
                output.append(self.alphabet[index])
            else:
                output.append(letter)
        return ''.join(output)
