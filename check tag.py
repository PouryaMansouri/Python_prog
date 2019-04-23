"""
Arpasland has surrounded by attackers. A truck enters the city. The driver claims the load is food and medicine from Iranians. Ali is one of the soldiers in Arpasland. He doubts about the truck, maybe it's from the siege. He knows that a tag is valid if the sum of every two consecutive digits of it is even and its letter is not a vowel. Determine if the tag of the truck is valid or not.

We consider the letters "A","E","I","O","U","Y" to be vowels for this problem.

Input Format

The first line contains a string of length 9. The format is "DDXDDD-DD", where D stands for a digit (non zero) and X is an uppercase english letter.

Output Format

Print "valid" (without quotes) if the tag is valid, print "invalid" otherwise (without quotes)
"""
vowels = ["A","E","I","O","U","Y"]
tag = input()
numbers, char =[tag[0:2],tag[3:6],tag[7:]] , tag[2]
valid = True
if char in vowels:
    valid = False
elif (int(numbers[0][0])+int(numbers[0][1]))%2 != 0:
    valid = False
elif (int(numbers[2][0])+int(numbers[2][1]))%2 != 0:
    valid = False
elif (int(numbers[1][0])+int(numbers[1][1]))%2 != 0:
    valid = False
elif (int(numbers[1][1])+int(numbers[1][2]))%2 != 0:
    valid = False


print('valid') if (valid) else print('invalid')