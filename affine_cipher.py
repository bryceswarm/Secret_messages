# Secret Messages program for Treehouse
#
# ** encrypts and decrypts messages **
#
# Author: Bryce Swarm

import string

from Secret_messages.ciphers import Cipher


class Affine(Cipher):
    """Encrypts and Decrypts a message using the Keyword cipher.
       Takes an input of a message, an alpha and beta keys.
       Alpha key must be prime number > 1 and < 26.
       Beta key can be any integer.
    """
    def __init__(self, alpha = None, beta = None):
        """Upon request of the Affine cipher, initializes.
           Requests and obtains alpha and beta keys, while verifying their
           validity.
           Calculates ciphertext list of indexes to apply to the alphabet."""

        self.alphabet = list(string.ascii_uppercase)
        self.cipher_list = []
        accepted_alpha = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

        # Ask for alpha key and verify its validity or take alpha key
        if not alpha:
            while True:
                try:
                    self.alpha = int(input('Please enter alpha key,' 
                                           ' should be an odd integer'
                                           ' from 3-25, except 13 \n> '))
                    if self.alpha in accepted_alpha:
                        break
                except ValueError:
                    print("Invalid alpha value")
        else:
            self.alpha = alpha

        # Ask for beta key or take beta key
        if not beta:
            self.beta = int(input('Please enter beta key, any integer 1-100\n> '))
        else:
            self.beta = beta

        # calculate cipher list of indexes
        for letter in self.alphabet:
            self.cipher_list.append(((self.alpha *
                                         self.alphabet.index(letter))
                                         + self.beta) % len(self.alphabet))


    # Encrypt user message using cipher list of indexes in alphabet
    def encrypt(self, text):
        """Encrypts the user message by matching the index of the entered
           letter to the cipher lists index, then matching back to the
           alphabet to obtain encrypted letter

           Example, if alpha == 5 and beta == 8:
           index of 'A' is 0
           cipher index of 0 is 8
           encrypted version of 'A' is 'I'
           as 'I' is index 8 on standard alphabet"""
        output = []

        for letter in text:
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                output.append(self.alphabet[self.cipher_list[index]])
            else:
                output.append(letter)
        return ''.join(output)

    # Decrypt user message using cipher list of indexes in alphabet
    def decrypt(self, text):
        """Decrypts the user message by matching the index of the entered
           letter to the cipher lists index, then matching back to the
           alphabet to obtain encrypted letter

           Example, if alpha == 5 and beta == 8:
           index of 'I' is 8
           cipher index of 8 is 0
           decrypted version of 'I' is 'A'
           as 'A' is index 0 on standard alphabet"""
        output = []

        for letter in text:
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                output.append(self.alphabet[self.cipher_list.index(index)])
            else:
                output.append(letter)
        return ''.join(output)