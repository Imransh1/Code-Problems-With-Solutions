# cook your dish here
T = int(input())
for i in range(T):
    X , Y = map(int, input().split(' '))
    if X>=1:
        print(X*Y)
    else:
        print("error")
    
    