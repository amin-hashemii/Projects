import random


letters_lower = "abcdefghijklmnopqrxtuvwxyz"
letter_upper = letters_lower.upper()
symbols = "!@#$%&*"
numbers = "1234567890"
letters = letters_lower + letter_upper + symbols + numbers


while True:

    pass_len = int(input('Enter the password length: '))
    pass_count = int(input('How many passwords do you want: '))
    for i in range(1, pass_count + 1):
        password = ""
        for j in range(1, pass_len + 1):
            password += random.choice(letters)
        print(f'Password number {i}: {password}')
    break
