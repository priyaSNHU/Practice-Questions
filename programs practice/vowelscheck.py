vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Enter the string in which you want to search for vowels: ')
new_vowels = []
for letter in word:
    if letter in vowels:
        if letter not in new_vowels:
            new_vowels.append(letter)
for vowel in new_vowels:
    print(vowel)
print('No vowels found')
