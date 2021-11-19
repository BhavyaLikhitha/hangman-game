import random
from hangman_art import stages, logo
from hangman_words import word_list
import emoji

print(logo)
print("WISHING YOU A GOOD LUCK😀")
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
# print(f"the chosen word from list is {chosen_word}🤫")
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("\nGuess a letter: ").lower()
    print("\n")

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"\nYou guessed {guess}, that's not in the word.\nYou lost a life💔.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lost the game.Better luck next time😊")
    
    if not "_" in display:
        game_is_finished = True
        print("You win🥳🥳")
        break

    print(stages[lives])