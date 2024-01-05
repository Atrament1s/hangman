import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
previous_guesses = []

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            print(stages[lives])
            break

    if guess not in chosen_word:
        if guess not in previous_guesses:
            lives -= 1
            if lives != 0:
                print(stages[lives])
                print(f"You guessed {guess}, that's not in the word. You lose a life!")
            if lives == 0:
                end_of_game = True
                print(stages[0])
                print(f"You guessed {guess}, that's not in the word. You lose a life!")
                print(f"You lose! The word was {chosen_word}!")

    if guess in previous_guesses:
        print(f"You've guessed {guess} before!")

    previous_guesses.append(guess)

    if lives != 0:
        print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
