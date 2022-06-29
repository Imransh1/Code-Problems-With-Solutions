T = int(input())
for testcases in range(T):
    P = int(input())
    if P >= 0 and P <= 1000:
        if P > 10 and P < 100:
            print(-1)
        elif P>=100 and P%100!=0:
            count = P // 100
            rem = P%100 + count
            if rem > 10:
                print(-1)
            else:
                print(rem)
        elif P >= 100 and P%100 == 0:
            print(P//100)
        elif P <= 10 and P >= 0:
            print(P)