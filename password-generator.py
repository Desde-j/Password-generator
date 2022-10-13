import random

                                 
print('     __________                                                    .___   ________                                         __                   ')
print('     \______   \_____     ______  ________  _  __ ____ _______   __| _/  /  _____/   ____    ____    ____ _______ _____  _/  |_   ____  _______   ')
print('      |     ___/\__  \   /  ___/ /  ___/\ \/ \/ //  _ \ \ _ __ \ /__ |  /   \  ___ _/ __ \  /    \ _/ __ \ \  __ \ \__  \ \   __\/ _ \ \_  __\  ')
print('      |    |     / __ \_ \___ \  \___ \  \     /(  <_> )|  | \// /_/ |  \    \_\  \ \ ___/ |   |  \ \ ___/ |  | \/ / __ \_|  | (  <_> )|  | \/  ')
print('      |____|    (____  //____  >/____  >  \/\_/  \____/ |__|   \____ |   \______  / \___  >|___|  / \___  >|__|   (____  /|__|  \____/ |__|     ')
print('                     \/      \/      \/                             \/          \/      \/      \/      \/             \/                       ')       

print('Welcome To Your Password Generator')                                                                                                                                                     


print('_____________________________________________________________________________________________________________________')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ@!£$%<^&*();.:/§?0123456789'

number = input('Amount of passwords to generate: ')
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nHere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
print(passwords)   