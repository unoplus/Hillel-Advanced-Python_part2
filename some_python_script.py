import random

evil_calculon = "\U0001F606"
mockery_calculon = "\U0001F923"
shushing_calculon = "\U0001F92B"
guess_num = random.randint(1, 100)
count = 0

print(f'Hey! My name is Calculon! I thought of a number from 1 to 100.\n'
      f'Do you think you can guess? {evil_calculon}')

while True:
    user_num = input('Enter your number, miserable little man: ')
    count += 1
    if user_num.isdigit():
        if int(user_num) == guess_num:
            print(f'You guessed my number {guess_num}... {shushing_calculon}\n'
                  f'Number of attempts: {count}')
            break
        elif int(user_num) < guess_num:
            print(f'Ha ha ha! Your number is less than mine! {mockery_calculon}')
        else:
            print(f'Ha ha ha! Your number is greater than mine! {mockery_calculon}')
    else:
        print(f'Oh you pathetic bag of bones, you are allowed to enter a number from 1 to 100,'
              f' try again! {mockery_calculon}')