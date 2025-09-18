import random

words = ["apple", "zebra", "chair", "music", "cloud"]
word = random.choice(words)
word_list = list(word)
blank_list = ["_"] * len(word)
lives = 6
print("Welcome to Hangman Game!")
print("Guess the word:")
print(" ".join(blank_list))

while lives > 0 and "_" in blank_list:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single letter (a-z).")
        continue

    if guess in word_list:
        print(f" Good guess! '{guess}' is in the word.")
        for i, letter in enumerate(word_list):
            if letter == guess:
                blank_list[i] = guess
    else:
        lives -= 1
        print(f" Wrong guess! You have {lives} lives left.")

    print(" ".join(blank_list))

if "_" not in blank_list:
    print("\n YOU WIN! The word was:", word)
else:
    print("\n GAME OVER! The word was:", word)