list = ['r' , 'g', 'o', 'b', 'r']

for i in range(len(list)-1):
    if( list[i] == 'b' and list[i+1]=='b'):
        print('the list contains 2 blues consucutively')
        break
else:
    print('the list desnot have any 2 blues consequitively')
    

        
    
