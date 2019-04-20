"""
There are 7 floors in BH3 and only 2 lifts.
 Initially Lift A is at the ground floor and Lift B at the top floor. 
 Whenever someone calls the lift from N th floor, the lift closest to that floor comes to pick him up. 
 If both the lifts are at equidistant from the N th floor, them the lift from the lower floor comes up.
 
 INPUT

First line contains a integer T denoting the number of test cases.

Next T lines contains a single integer N denoting the floor from which lift is called.

OUTPUT

Output T lines containing one character "A" if the first lift goes to N th floor or "B" for the second lift.
"""

class lift():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def difrence(self, n):
        self.dif = abs(self.position - n)
        return self.dif
    

def choose(lift_a,lift_b,n):
    a = lift_a.difrence(n)
    b = lift_b.difrence(n)
    if a>b :
        print(lift_b.name)
        lift_b.position = n
    elif a<b:
        print(lift_a.name)
        lift_a.position = n
    else:
        if lift_a.position<lift_b.position:
            print(lift_a.name)
            lift_a.position = n
        else:
            print(lift_b.position)
            lift_b.position = n




T = int(input())
lift_a = lift('A',0)
lift_b = lift('B',7)
for i in range(0,T):
    N = int(input())
    choose(lift_a,lift_b,N)
