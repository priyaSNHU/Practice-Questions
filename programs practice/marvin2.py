string = 'Marvin the paranoid android'
letter = list(string)

for char in letter[:6]:
    print('\t', char)

for char in letter[-7:]:
    print('\t' * 2, char)

for char in letter[7:20:2]:
    print('\t'*3, char)
