moves=input()
location = [0,0]
for move in moves:
    if move=='L':
        location[0] -= 1
    elif move=='R':
        location[0] += 1
    elif move=='U':
        location[1] += 1
    elif move=='D':
        location[1] -= 1
print(location[0],location[1])
