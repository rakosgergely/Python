lower = 3
upper = 1000000000


for num in range(lower, upper + 1):
    if num > 1:
        prim = False
        for i in range(2, num):
            if (num % i) == 0:
                prim = False
                break
            else:
                prim = True
        if prim is True:
            print(num)

