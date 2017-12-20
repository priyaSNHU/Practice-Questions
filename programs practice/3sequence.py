list = ['r' , 'r', 'b', 'b', 'b']

for i in range(len(list)-1):
    if( list[i] == 'r' and list[i+1]=='r' and ((list[i+2] == 'r') or (list[i+2] == 'b'))):
        print('The sequence is maintained')
        break
else:
    print('The sequence is not maintained')

        
    
