vowels = {'a', 'e','i','o','u'}
word = input("Enter your string: ")
letter = vowels.intersection(set(word))
print(letter)


