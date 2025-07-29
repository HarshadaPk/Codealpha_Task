import random

words = ["apple", "tiger", "plane", "chair", "mouse"]
word = random.choice(words)
guessed = []
chances = 6

print(" Hangman Game!")
print("_ " * len(word))

while chances > 0:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("! Enter a single letter.")
        continue

    if guess in guessed:
        print("Already guessed.")
        continue

    guessed.append(guess)

    if guess in word:
        print(" Correct!")
    else:
        chances -= 1
        print(f" Wrong! Attempts left: {chances}")

    # Show current progress
    display = [letter if letter in guessed else "_" for letter in word]
    print(" ".join(display))

    if "_" not in display:
        print(" You won!")
        break
else:
    print(f" You lost! The word was '{word}'.")
