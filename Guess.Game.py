secret_word = "Rod"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("This is your number " + str(guess_count + 1) + " attempt. Enter the secret word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry, you attempted " + str(guess_count) + " times, you are out of the game")
else:
    print("Congratulations you win")