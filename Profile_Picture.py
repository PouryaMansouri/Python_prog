l = int(input())
n = int(input())
for i in range(0,n):
    w, h =map(int,input().split())
    if w<l or h<l :
        print("UPLOAD ANOTHER")
    else:
        if w==h:
            print("ACCEPTED")
        else:
            print("CROP IT")
