# cook your dish here
T = int(input())
for testcases in range(T):
    X , Y = map(int,input().split(' '))
    if X >=1 and X < Y and Y<= 100:
        if (X* 3) < (Y*2):
            print(X*3)
        else:
            print(Y*2)
    else:
        print("X must be less than Y")