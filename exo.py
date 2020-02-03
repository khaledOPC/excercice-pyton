# Je créer la fonction def get_number_of_vowels

def get_number_of_vowels(word):
	return sum(1 for letter in word if letter in "aeiouyAEIOUY")

print(get_number_of_vowels("Openclassroom"))