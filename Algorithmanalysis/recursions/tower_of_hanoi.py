def tower_of_hanoi(disks , from_pole, to_pole, with_pole):
    if disks >= 1:
        tower_of_hanoi(disks - 1 , from_pole, with_pole, to_pole)
        print(" Move" , disks," from " + from_pole + " to " + to_pole )
        tower_of_hanoi(disks-1, with_pole,  to_pole, from_pole)
    



disk = int(input ("enter the no of disks : "))
tower_of_hanoi(disk , 'A' , 'B', 'C')



    
