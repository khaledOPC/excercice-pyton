def get_number_of_vowels(word):



	nb_of_vowels = 0

	for letter in word:
		if letter in "aeiouy":
			nb_of_vowels += 1
	return nb_of_vowels


word = input("Entrez votre mot")
print("Il y'a",get_number_of_vowels(word),"voyelle dans le mot",word)