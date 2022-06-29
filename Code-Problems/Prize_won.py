# cook your dish here
T = int(input())
for testcases in range(T):
    X , Y = map(int,input().split(' '))
    if X >= Y and X <=1000 and Y >= 1:
        total_prize_won = (X*10) + (Y*90) 
        print(total_prize_won)
    else:
        print("wrong values")
