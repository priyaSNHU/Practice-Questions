def search_for_letters(phrase:str, letters:str) -> set:
    """ print vowels found in provided word"""
    return set(letters).intersection(set(phrase))

search_for_letters('priyanka', 'aeiou')
search_for_letters('prudhvi', 'priyanka')
