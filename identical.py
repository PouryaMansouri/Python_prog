
t = int(input())
for i in range(t):
    s1, s2 = map(list,input().split())
    if sorted(s1) == sorted(s2):
        print('YES')
    else:
        print('NO')