import encode
import decode
import art

print(art.logo)


def caesar(direction, text, shift):
    modified_text = ""
    if direction == 'encode':
        modified_text = encode.encrypt(text, shift)
    elif direction == 'decode':
        modified_text = decode.decrypt(text, shift)
    else:
        print("Invalid direction. Please type 'encode' or 'decode'.")
    return modified_text



should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    caesar(direction, text, shift)
    res = input("Type 'yes' if you want to continue, otherwise type 'no':\n")
    if res.lower() != 'yes':
        should_continue = False
        print("Goodbye")
        print("\n")