import random
import string

class bcolors:
	ok = "\033[1;37;42m"
	wrong = "\033[1;37;41m"
	maybe = "\033[1;37;104m"
	reset = "\033[0m"

class phrases:
	greeting = "this is my game. play."
	buffering = "choosing a word for you..."
	instructions = "guess a 5 letter word in 6 tries"
	done = "done! you can start guessing!"
	guess = "your guess: "
	lang = "pick a language:"
	choice = "you chose"

class dictionaries:
	languages = {
		"italian": "parole.txt",
		"english": "words.txt"
	}

def random_line(afile):
	line = next(afile)
	for num, aline in enumerate(afile, 2):
		if random.randrange(num):
			continue
		line = aline
	return line

def get_random_word(lang):
	word_file = dictionaries.languages[lang]

	with open(word_file, "r") as f:
		word = random_line(f)

	word = word[:5]
	return word

def take_a_guess():
	guess = ""

	while len(guess) != 5 or not guess.isalpha():
		guess = input(phrases.guess)
		guess = guess.lower()

	return guess    

def find_matching_letters(word, guess):
	matching = []
	for i, letter in enumerate(word):
		if letter == guess[i]:
			matching.append(i)

	return matching

def cli_UI(options, label):
	for i in range(len(options)):
		print('{})'.format(i + 1), options[i])
	
	choice = -1
	while not str(choice).isnumeric() or int(choice) - 1 not in range(len(options)):
		choice = input(label)
	
	choice = int(choice) - 1
	print('{} {}'.format(phrases.choice, options[choice]))
	return choice

def main():
	print(phrases.greeting + "\nINsTruCtioNs:" + phrases.instructions)

	languages = list(dictionaries.languages.keys())
	language = languages[cli_UI(languages, phrases.lang)]

	print(phrases.buffering)
	word = get_random_word(language)

	print("\n" + phrases.done + "\n")
	for _ in range(6):
		guess = take_a_guess()
		matching_indexes = find_matching_letters(word, guess)

		for i, letter in enumerate(guess):
			if i not in matching_indexes:
				color = bcolors.wrong
			elif letter in word:
				color = bcolors.maybe
			if i in matching_indexes:
				color = bcolors.ok

			print(f"{color}{letter}{bcolors.reset}", end=" ")

		if word == guess:
			return f"You won! The word was {word}"

		print()

	return f"Nooo, you lost. The word was {word}"

print(main())