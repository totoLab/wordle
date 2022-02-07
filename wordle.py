import random

class Bcolors:
	ok = "\033[1;37;42m"
	wrong = "\033[1;37;41m"
	maybe = "\033[1;37;104m"
	reset = "\033[0m"

class Phrases:
	greeting = "this is my game. play."
	buffering = "choosing a word for you..."
	instructions = "INsTruCtioNs: guess a 5 letter word in 6 tries"
	done = "done! you can start guessing!"
	guess = "your guess: "
	lang = "pick a language:"
	choice = "you chose"
	won = "You won! The word was"
	lost = "Nooo, you lost. The word was"
	retry = 'retry'

class InputErrors:
	length = 'length of guess is not 5.'
	chars = 'some characters in guess are not alphabetic.'
	dictionary = 'the guessed word is not in the dictionary.'

class Dictionaries:
	languages = {
		"italian": "parole.txt",
		"english": "words.txt"
	}

def create_language_set(lang):
	filename = Dictionaries.languages[lang]
	return set(map(str.strip, open(filename)))

def random_line(afile):
	line = next(afile)
	for num, aline in enumerate(afile, 2):
		if random.randrange(num):
			continue
		line = aline
	return line

def get_random_word(lang):
	word_file = Dictionaries.languages[lang]

	with open(word_file, "r") as f:
		word = random_line(f)

	word = word[:5]
	return word

def take_a_guess(lang):
	guess = ""
	dictionary = create_language_set(lang)
	ok = True

	while ok:
		guess = input(Phrases.guess)
		guess = guess.lower()

		if len(guess) != 5:
			print(InputErrors.length, Phrases.retry)
		elif not guess.isalpha():
			print(InputErrors.chars, Phrases.retry)
		elif guess not in dictionary:
			print(InputErrors.dictionary, Phrases.retry)
		else:
			ok = False

	return guess    

def find_matching_letters(word, guess):
	matching = []
	for i, letter in enumerate(word):
		if letter == guess[i]:
			matching.append(i)

	return matching

def cli_ui(options, label):
	for i, option in enumerate(options):
		print(f'{i + 1}) {option}')
	
	choice = -1
	while not str(choice).isnumeric() or int(choice) - 1 not in range(len(options)):
		choice = input(label)
	
	choice = int(choice) - 1
	print(f'{Phrases.choice} {options[choice]}')
	return choice

def main():
	print(Phrases.greeting + "\n" + Phrases.instructions)

	languages = list(Dictionaries.languages.keys())
	language = languages[cli_ui(languages, Phrases.lang)]

	print(Phrases.buffering)
	word = get_random_word(language)

	print("\n" + Phrases.done + "\n")
	for _ in range(6):
		guess = take_a_guess(language)
		matching_indexes = find_matching_letters(word, guess)

		for i, letter in enumerate(guess):
			if i not in matching_indexes:
				color = Bcolors.wrong
			elif letter in word:
				color = Bcolors.maybe
			if i in matching_indexes:
				color = Bcolors.ok

			print(f"{color}{letter}{Bcolors.reset}", end=" ")

		if word == guess:
			return f"{Phrases.won} {word}"

		print()

	return f"{Phrases.lost} {word}"

print(main())
