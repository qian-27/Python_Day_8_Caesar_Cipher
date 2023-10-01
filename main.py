alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Another solution of out of range error.
# alphabet = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
#     'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
#     't', 'u', 'v', 'w', 'x', 'y', 'z'
# ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

alphabet_list_length = len(alphabet)


#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
def encrypt(plain_text, shift_amount):
    encrypt_text = ""
    for character in plain_text:
        i = alphabet.index(character)
        i += shift_amount
        # if
        if i >= alphabet_list_length:
            i = i - alphabet_list_length
        new_character = alphabet[i]
        encrypt_text += new_character

    print(f"The encoded text is {encrypt_text}")


#Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
def decrypt(cipher_text, shift_amount):
    decrypt_text = ""
    for character in cipher_text:
        i = alphabet.index(character)
        i -= shift_amount
        new_character = alphabet[i]
        decrypt_text += new_character

    print(f"The decoded text is {decrypt_text}")

    #Then call the correct function based on that 'drection' variable.
#Then call the correct function based on that 'drection' variable. 


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
