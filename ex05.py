import random

cmp = random.randint(1,100)
while True:
  guess = float(input('Guess a number between 1 and 100:'))

  if guess == cmp:
    print('Correct!!')
    break
  if guess != cmp:
    print('Not Correct!!')
    if 1 <= guess < cmp:
        print('Guess a large number!')
    elif 100 >= guess > cmp:
        print('Guess a small number!') 
    elif guess > 100 or guess < 1:
        print('The number must between 1~100!')
    
    continue
  print('n')
else:
  print('else')
