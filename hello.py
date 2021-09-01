import time

print('hello world') # output to terminal. Command: python hello.py
name = input('what is your name: ') # input from terminal
print('its nice to meet you ' + name)
age = input('how old are you?: ')
print('wow, ' + age + ', You are very old!')
time.sleep(2)
dev_since = input('What year did you start developing? ')
since = 2021 - int(dev_since)
print('Oh, cool! You have been developing for '+ str(since) + ' years.')

# this is a test