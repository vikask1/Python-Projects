# Tap On Run To Start Playing.

import random

Random = random.randint(1111,9999)

print('GUESS THE NUMBER\n\n')

name = input('Enter Your Name: ')

print(f'hii detective {name}, try to guess the correct number between 1111 and 9999')

def main():

  guess = int(input('\nEnter Your Guess: '))

  if str(guess) == str(Random):

    print('Correct Guess!')

  else:

    print('Incorrect Guess!')

    print(f'correct answer = {Random}')

while 2 == 2:

  try: 

    main()

  except ValueError:

    print('Please enter a integer value between 1111 and 9999.')

