"""
Patlu and Motu works in a building construction, they have to put some number of bricks N from one place to another, and started doing their work. They decided , they end up with a fun challenge who will put the last brick.

They to follow a simple rule, In the i'th round, Patlu puts i bricks whereas Motu puts ix2 bricks.

There are only N bricks, you need to help find the challenge result to find who put the last brick.

Input:

First line contains an integer N.

Output:

Output "Patlu" (without the quotes) if Patlu puts the last bricks ,"Motu"(without the quotes) otherwise.

Constraints:

1 ≤ N ≤ 10000
"""
n = int(input())
counter = 1
while(True):
    p = counter
    n -= p
    if n<=0 :
        print('Patlu')
        break
    m = counter * 2
    n -= m
    if n<=0 :
        print('Motu')
        break
    counter += 1