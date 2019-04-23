from datetime import datetime
n = int(input())
for i in range(n):
    string = input().split()
    t1 = string[0] + ' ' + string[1]
    t2 = string[2] + ' ' + string[3]
    FMT = '%H %M'
    tdelta = datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT)
    worktime = str(tdelta).split(':')
    print(int(worktime[0]),int(worktime[1]))