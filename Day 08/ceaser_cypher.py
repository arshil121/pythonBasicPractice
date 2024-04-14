from alphabets import alphabet
from art import logo

print(logo)


def caesar(direction, text, shift):
    result_text = ""
    if direction == "decode":
        shift *= -1  # If we're decoding, we reverse the direction of the shift

    for letter in text:
        if letter in alphabet:  # Check if the letter is in the alphabet
            position = alphabet.index(letter)
            new_position = (position + shift) % len(alphabet)
            result_text += alphabet[new_position]
        else:
            result_text += letter

    # Print the result based on the direction
    if direction == "encode":
        print(f"Encrypted Text is {result_text}")
    elif direction == "decode":
        print(f"Decrypted Text is {result_text}")
    else:
        print("Wrong Input")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid direction. Please type 'encode' or 'decode'.")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        caesar(direction=direction, text=text, shift=shift)
        result = input("Do you want to continue: Yes/No: ").lower()
        if result == "no":
            should_continue = False
            print("Good Bye!")
