alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
    result = ""
    for c in text: # def
        if c in alphabet: # d 
            position = alphabet.index(c) # 3
            new_position = (position - shift) %len(alphabet)
            shifted_char = alphabet[new_position]
            result += shifted_char
        else:
            result += c
        
    print(result)

        

        
#TODO-2: Inside the 'decrypt()' function, shif each letter of the 'text' forwards in the
# alphabet backwards by the shift amount and print the decrypted text


#TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one/single function
# which called caesar()
# Use the value of the user chosen 'direction' variable to determine which functionality to use.
# call the caesar function instead of encrypt/decrypt and 
# pass in all three variables direction/text/shift