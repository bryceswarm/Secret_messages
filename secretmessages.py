# Secret Messages program for Treehouse
#
# ** encrypts and decrypts messages **
#
# Author: Bryce Swarm

import os

from affine_cipher import Affine
from caesar_cipher import Caesar
from keyword_cipher import Keyword
from atbash_cipher import Atbash


# clear the command screen
def clear_screen():
    """ Clears the command screen for next prompts to be displayed
        more efficiently."""
    os.system('cls' if os.name == 'nt' else 'clear')


def secret_messages():
    """ Performs the user prompts and determines which cipher to implement.
        Also performs prompts and determines whether to Encrypt or Decrypt
        the message."""

    cipher_dict = {
        'CAESAR': Caesar,
        'ATBASH' : Atbash,
        'KEYWORD' : Keyword,
        'AFFINE' : Affine
    }
    encryption_options = {
        'E' : 'Encrypt',
        'D' : 'Decrypt'
    }

    cipher_list = [''.join(key.title()) for key in cipher_dict]

    while True:
        clear_screen()
        print('Welcome, Secret Agent.\n'
              'Select one of the following ciphers:\n'
              'Enter "QUIT" to quit.\n')

        # print cipher list
        for cipher in cipher_list:
            print('-{cipher}'.format(cipher = cipher))

        # take user input on which cipher they want
        cipher_input = input('\n> ').upper()

        # check validity of cipher and operate 'Quit' option
        while True:
            if cipher_input == 'QUIT':
                cipher_active = None
                break
            try:
                cipher_active = cipher_dict[cipher_input]()
                break
            except KeyError:
                cipher_input = input('That is not a valid cipher,'
                                     ' please choose again.\n> ').upper()

        if not cipher_active:
            break

        # analyze input
        clear_screen()
        print("You have selected '{cipher}':\n"
              "Press 'E' to Encrypt or "
              "'D' to Decrypt:".format(cipher = cipher_input))
        encrypt_decrypt_input = input('> ').upper()

        # check validity of encrypt/decrypt choice
        while True:
            try:
                encrypt_choice = encryption_options[encrypt_decrypt_input]
                break
            except KeyError:
                encrypt_decrypt_input = input("Invalid Entry,"
                                              " only 'E' and 'D'"
                                              " are accepted\n> ").upper()
                continue

        # Encrypt message
        if encrypt_choice == 'Encrypt':
            print('What is the message you would like to encrypt?')
            encrypt_message = input('> ').upper()
            print(cipher_active.encrypt(encrypt_message))
            break
        # Decrypt message
        elif encrypt_choice == 'Decrypt':
            print('What is the message you would like to decrypt?')
            decrypt_message = input('> ').upper()
            print(cipher_active.decrypt(decrypt_message))
            break


if __name__ == '__main__':
    # runs entire program
    secret_messages()
