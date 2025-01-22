import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*().,[]{}'

number = int(input('Enter amount of Password: '))

length = int(input('Lenght of password: '))

for pwd in range(number):
    password = ''
    for len in range(length):
        password += random.choice(chars)
        
    print(password)

