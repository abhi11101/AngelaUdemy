def encrypt(input_string, shift_num):
    encrypted_string = ""
    print(shift_num%25)
    for i in input_string:
        index = alphabets.index(i)
        index = (index+shift_num)%25
        newChar = alphabets[index]
        encrypted_string += newChar

    print(encrypted_string)


def decrypt(input_string, shift_num):
    decrypted_string = ""
    inputStringlength = len(input_string)
    for i in range(inputStringlength):
        index = alphabets.index(input_string[i])
        index = (index-shift_num) % 25
        newChar = alphabets[index]
        decrypted_string += newChar

    print(decrypted_string)


alphabets = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']


def work():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    input_string = input("Type your message: ")
    shift_num = int(input("Type the number: "))

    if direction == "encode":
        encrypt(input_string.lower(), shift_num)
    elif direction == "decode":
        decrypt(input_string.lower(), shift_num)

work()