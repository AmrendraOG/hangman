from hangman_word import word_list
from hangman_art import hangman_states
import random

game_ended = False

life = 0

word = random.choice(word_list).lower()
secret = []

print(f"Word is {word} \n")

for _ in range(len(word)):
  secret.append("_")

while not game_ended:
  
  if life != len(hangman_states):
    guessed_letter = input("Guess the letter: ").lower()
    print("\n")

    if guessed_letter not in word:
      print(f"{guessed_letter} is not in the word. You lose a life!\n")
      print(f"{hangman_states[life]}\n")
      life += 1

    for i in range(len(word)):
      if word[i] == guessed_letter:
        secret[i] = guessed_letter

    if "_" not in secret:
      game_ended = True
      print("You win!")
  else:
    print("You lose!")
    break
