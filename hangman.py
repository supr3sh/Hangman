import random
import os
from words import words

def get_word():
	word= random.choice(words)
	return word.upper()

def play(word):
	uncomplete_word= "_"* len(word)
	guessed=False
	guessed_letters = []
	guessed_words = []
	tries=6
	print("HANGMAN!!")
	print(display_hangman(tries))
	print(uncomplete_word)
	print("Length of the word is ",len(word))
	print("\n")
	while not guessed and tries>0:
		guess = input("Please guess a letter or a word: ").upper()
		if len(guess) == 1 and guess.isalpha():
			if guess in guessed_letters:
				print("You already guessed the letter ",guess)
			elif guess not in word:
				print(guess," is not in the word.")
				tries = tries - 1
				guessed_letters.append(guess)
			else:
				print("Good job")
				guessed_letters.append(guess)
				word_list = list(uncomplete_word)
				indices = [i for i,letter in enumerate(word) if letter == guess]
				for index in indices:
					word_list[index] = guess
				uncomplete_word = "".join(word_list)
				if "_" not in uncomplete_word:
					guessed = True
		elif len(guess) == len(word) and guess.isalpha():
			if guess in guessed_words:
				print("You already guessed the word ",guess)
			elif guess!= word:
				print(guess," is not the word.")
				tries -= 1
				guessed_words.append(guess)
			else:
				guessed = True
				uncomplete_word = word
		else:
			print("Not a valid guess.")
		print(display_hangman(tries))
		print(uncomplete_word)
		print("\n")
	if guessed:
		print("Congrats!! You've won")
	else:
		print("Sorry,you ran out of tries. The word was "+ word +". Maybe next time!")
		
def display_hangman(tries):
	stages = [ """
				  ---------------------
				  |		  |
				  |		  O
				  |		 \\|/
				  |		  |
				  |		 / \\
				  |
				  |
				  |
				  -
			   """,
			   """
				  ---------------------
				  |		  |
				  |		  O
				  |		 \\|/
				  |		  |
				  |		 /
				  |
				  |
				  |
				  -
			   """,
			   """
			      ---------------------
				  |		  |
				  |		  O
				  |		 \\|/
				  |		  |
				  |
				  |
				  |
				  |
				  -
			   """,
			   """
			      ---------------------
				  |		  |
				  |		  O
				  |		 \\|
				  |		  |
				  |
				  |
				  |
				  |
				  -
			   """,
			   """
			      ---------------------
				  |		  |
				  |		  O
				  |		  |
				  |		  |
				  |
				  |
				  |
				  |
				  -
			   """,
			   """
			      ---------------------
				  |		  |
				  |		  O
				  |
				  |
				  |
				  |
				  |
				  |
				  -
			   """,
			   """
			      ---------------------
				  |		  |
				  |
				  |
				  |
				  |
				  |
				  |
				  |
				  -
			   """
		]
	return stages[tries]
			   
def main():
	word = get_word()
	play(word)
	while input("Play Again? (Y/N) ").upper() == "Y":
		word = get_word()
		play(word)
		
if __name__ == "__main__":
	main()
