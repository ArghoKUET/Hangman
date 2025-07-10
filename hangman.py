import random
import hangman_ascii
import words

choosen_word = random.choice(words.word_list)
print(choosen_word)
placeholder_list = []
placeholder = ""
placeholder_f = ""
correct_guess = ""
lives = 6
incorrect_count = 0
for i in choosen_word:
    placeholder_list.append("_")
for i in placeholder_list:
    placeholder += i
print(placeholder)

while not placeholder_f == choosen_word:
    print(f"You Have {lives} lives left!!")
    correct_count = 0
    guess = input("Guess a letter from the word: ").lower()
    if guess in correct_guess:
        print("You already guessed that correct letter!")
        continue
    index = 0
    for i in choosen_word:
        index += 1
        if i == guess:
            correct_count += 1
            placeholder_list[index - 1] = guess
            correct_guess += guess
    if correct_count == 0:
        lives -= 1
        incorrect_count += 1
        print("Wrong Answer. Hangman is in Danger")
        print(hangman_ascii.HANGMANPICS[incorrect_count - 1])
    if lives == 0:
        break
    placeholder_f = ""
    for i in placeholder_list:
        placeholder_f += i
    print(placeholder_f)
if lives == 0:
    print("You are lost! Hangman is hanged:(")
else:
    print("Yes!! you Did it. Hangman is alive!!")
