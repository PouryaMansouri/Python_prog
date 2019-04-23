seats_position = {}
for i in range(1,109,12):
    seats_position[i]='{} WS'.format(i+11)
    seats_position[i+1]='{} MS'.format(i+10)
    seats_position[i+2]='{} AS'.format(i+9)
    seats_position[i+3]='{} AS'.format(i+8)
    seats_position[i+4]='{} MS'.format(i+7)
    seats_position[i+5]='{} WS'.format(i+6)
    seats_position[i+6]='{} WS'.format(i+5)
    seats_position[i+7]='{} MS'.format(i+4)
    seats_position[i+8]='{} AS'.format(i+3)
    seats_position[i+9]='{} AS'.format(i+2)
    seats_position[i+10]='{} MS'.format(i+1)
    seats_position[i+11]='{} WS'.format(i)
T = int(input())
N = []
for i in range(0,T):
    N.append(int(input()))
for i in N:
    print(seats_position[i])