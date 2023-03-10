import random
import string
# Rotor settings for the Enigma machine

rotor1 = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
rotor2 = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
rotor3 = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']

# Reflector setting for the Enigma machine
reflector = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']

# Plugboard setting for the Enigma machine
plugboard = {'A': 'M', 'B': 'F', 'C': 'L', 'D': 'T', 'E': 'X', 'G': 'K', 'H': 'N', 'I': 'O', 'J': 'P', 'Q': 'S', 'R': 'U', 'V': 'Y', 'W': 'Z'}

# Function to rotate the rotor
def rotate_rotor(rotor):
    return rotor[1:] + [rotor[0]]
    
# Function to encrypt a single letter using the Enigma machine
rotate_count = 0 #define rotate_count
def enigma_letter(letter, rotor1, rotor2, rotor3, reflector, plugboard):
    global rotate_count
    # First, pass the letter through the plugboard
    letter = letter.upper()
    letter = plugboard.get(letter, letter)
    # Pass the letter through the rotors
    if letter in string.ascii_uppercase:
        letter_index = ord(letter) - ord('A')
        rotor1_output = rotor1[letter_index]
        rotor2_output = rotor2[ord(rotor1_output) - ord('A')]
        rotor3_output = rotor3[ord(rotor2_output) - ord('A')]
        reflector_output = reflector[ord(rotor3_output) - ord('A')]
    #Apply plugboard substitutions and teturn encrypted letter
    # Pass the letter through the reflector
    letter_index = reflector_output
    print("Letter index:", letter_index)
    # Pass the letter back through the rotors in reverse order
    letter_index = rotor3.index(letter_index)
    print("Letter index:", letter_index)
    #letter = chr(letter_index) + ord('A')
    letter_index = rotor2[ord(rotor3_output) - ord('A')]
    print("Letter index:", letter_index)
    letter_index = rotor1.index(letter_index)
    
    # Pass the letter back through the plugboard
    letter = chr(letter_index + ord('A'))
    letter = plugboard.get(letter, letter)
    
    # Rotate the rotors
    rotor1 = rotate_rotor(rotor1)
    rotate_count += 1
    if rotate_count % 26 == 0:
        rotor2 = rotate_rotor(rotor2)
    if rotate_count % (26*26) == 0:
        rotor3 = rotate_rotor(rotor3)

    print("Rotors after rotation:")
    print(rotor1, rotor2, rotor3)

    return letter
    
def encrypt_message(message):
    encrypted_text = "" # initialize encrypted_text as an empty string
    for letter in message:
        # encrypt each letter using the enigma_letter function and add it to encrypted_text
        encrypted_text += enigma_letter(letter, rotor1, rotor2, rotor3, reflector, plugboard)
    return encrypted_text

# Prompt the user for a message
message = input("Enter a message to encrypt: ")

# Encrypt the message
encrypted_text = encrypt_message(message)

def write_to_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

# Write the encrypted message to a file
write_to_file('encrypted_message.txt', encrypted_text)


print('Encryption complete!')
print('Encrypted file saved to: encrypted_message.txt')

