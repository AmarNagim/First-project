import time
import sys

print('hello world') # output to terminal. Command: python hello.py
name = input('Wat is je volledige naam?: ') # input from terminal

if name == ('Amar Nagim'): print('Aangenaam, ' + name + '.')
else: 
     sys.exit('Helaas zit je niet in ons database, ' + name + '.')

time.sleep(1)

age = int(input('Hoe oud ben je?: ')) # age
if age > int(17): print('Je bent ' + str(age) + ' jaar oud. Ga door naar de volgende vraag.')
else: 
    sys.exit('Helaas kunt u niet doorgaan vanwege uw leeftijd.')

dev_since = input('Welk jaar ben je begonnen met programmeren? ')                                                          # Developing since
since = 2021 - int(dev_since)
print('Oh, cool! Je bent al '+ str(since) + ' jaar aan het programmeren!')
time.sleep(1)


print('Nu ik weet wie je bent ga ik je laten zien wat ik kan.')                   # Math
time.sleep(1)
print('Je gaat me twee waardes geven. Deze zal ik bij elkaar optellen en het antwoord ervan laten zien.')

first = input('Eerste waarde: ')
second = input ('Tweede waarde: ')
sum = float(first) + float(second)
print ('Antwoord: ' + str(sum))
time.sleep(1)

print('Bij de volgende mag je zelf kiezen of je een optel of aftrek som maakt. Gebruik + of -.')
calculation1 = input('Eerste waarde: ')
sum_sub = input('optellen of aftrekken: ')
calculation2 = input('Tweede waarde: ')


if sum_sub == ('-'): answer = float(calculation1) - float(calculation2)
else:
    answer = float(calculation2) + float(calculation1)
print('Het antwoord is: ' + str(answer))