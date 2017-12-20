def anagramSol():
    s1 = 'priyanka'
    s2 = list('priya')
    pos1 = 0
    found = True
    while pos1 < len(s1) and found:    
        pos2 = 0
        is_found = False
        while pos2 < len(s2) and not is_found:
            if s1[pos1] == s2[pos2]:
                is_found = True
            else:
                pos2 = pos2+1

        if is_found:
            s2[pos2] = None
        else:
            found = False
        pos1 =pos1 + 1

    return found


        

    
print(anagramSol())
