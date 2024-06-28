print('[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]')
print(['G','G','G','-','B','B','B'])
positions=['G','G','G','-','B','B','B']
positions2=positions[::-1]
while True:
    i = input("Press q to quit else \nEnter position:")
    if i =='q' or i=='Q':
        print('You Lose')
        break
    i = int(i)
    if i<0 or i>6:
        print('Invalid Move')
        continue
    elif positions[i] == "-":
        print("Invalid Move")
        continue
    pos2=0
    if positions[i] == 'G':
        if i+1<=6 and positions[i+1]=="-":
            pos2=(i+1)
        elif i+2<=6 and positions[i+2]=="-":
            pos2=(i+2)
        else:
            print("Invalid Move")
            continue
    elif positions[i]=="B":
        if i-1>=0 and positions[i-1]=="-":
            pos2=(i-1)
        elif i-2>=0 and positions[i-2]=="-":
            pos2=(i-2)
        else:
            print("Invalid Move")
            continue
            
    temp = positions[i]
    positions[i] = positions[pos2]
    positions[pos2] = temp
    print('[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]')
    print(positions) 
    if positions2 == positions:
        print("You Won")
        break

    
        
    
