secret_no = 5
guess_count = 0
guess_limit = 3
while guess_count <= guess_limit :
    user_guess = int(input('Guess: '))
    guess_count += 1
    if (user_guess == secret_no):
        print("YOU WON!")
        break
else:
    print("Lost It, Better Luck Next Time")