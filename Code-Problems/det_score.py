T = int(input())
for i in range(T):
    X , N = map(int, input().split(' '))
    if X>=10 and X <=200 and N>=0 and N<= 10:
        print(X//10 * N)
    else:
        print("error")
    