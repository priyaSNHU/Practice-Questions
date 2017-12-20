def perm(s1,s2):

    if len(s1) == len (s2):
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    return True
                else:
                    return False
    else:
        return False


print(perm( 'god' , 'cat'))


def per(s1,s2):

    no_char = 256

    count1 = [0] * no_char
    count2 = [0] * no_char

    for i in s1:
        count1[ord(i)]+= 1
    for i in s2:
        count2[ord(i)]+= 1

    if len(s1) != len(s2):
        return False

    for i in range(no_char):
        if (count1[i]) != (count2[i]):
            return False

    return True

if  per('priya', 'riyap'):
    print('permutation to each other')
else:
    print('not permutation to each other')
    
        
        
