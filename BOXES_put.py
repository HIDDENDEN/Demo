a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
mymax1, med1, mymin1 = 0, 0, 0
if a1 > b1:
    if a1 > c1:
        if b1 > c1:
            (mymax1, med1, mymin1) = (a1, b1, c1)
        else:
            (mymax1, med1, mymin1) = (a1, c1, b1)
    else:
        (mymax1, med1, mymin1) = (c1, a1, b1)
else:  # b>a
    if b1 > c1:
        if a1 > c1:
            (mymax1, med1, mymin1) = (b1, a1, c1)
        else:
            (mymax1, med1, mymin1) = (b1, c1, a1)
    else:
        (mymax1, med1, mymin1) = (c1, b1, a1)

# print("First BOX = ", end="")
# print(mymax1, med1, mymin1)
mymax2, med2, mymin2 = 0, 0, 0
if a2 > b2:
    if a2 > c2:
        if b2 > c2:
            (mymax2, med2, mymin2) = (a2, b2, c2)
        else:
            (mymax2, med2, mymin2) = (a2, c2, b2)
    else:
        (mymax2, med2, mymin2) = (c2, a2, b2)
else:  # b>a
    if b2 > c2:
        if a2 > c2:
            (mymax2, med2, mymin2) = (b2, a2, c2)
        else:
            (mymax2, med2, mymin2) = (b2, c2, a2)
    else:
        (mymax2, med2, mymin2) = (c2, b2, a2)
# print("Second BOX = ", end="")
# print(mymax2, med2, mymin2)
if (mymax1 == mymax2) and (med1 == med2) and (mymin1 == mymin2):
    print("Boxes are equal")
else:
    f1, f2, f3 = 0, 0, 0
    if mymax1 > mymax2:
        f1 = 1
    elif mymax1 == mymax2:
        f1 = 0
    else:
        f1 = -1
    if med1 > med2:
        f2 = 1
    elif med1 == med2:
        f2 = 0
    else:
        f2 = -1
    if mymin1 > mymin2:
        f3 = 1
    elif mymin1 == mymin2:
        f3 = 0
    else:
        f3 = -1
    # print("Flags = ", end="")
    # print(f1, f2, f3)
    if (f1 > 0) or (f2 > 0) or (f3 > 0):
        if f1 == 0:
            f1 = 1
        if f2 == 0:
            f2 = 1
        if f3 == 0:
            f3 = 1
    if (f1 < 0) or (f2 < 0) or (f3 < 0):
        if f1 == 0:
            f1 = -1
        if f2 == 0:
            f2 = -1
        if f3 == 0:
            f3 = -1
    if f1 == f2 == f3:
        if f1 > 0:
            print("The first box is larger than the second one")
        else:
            print("The first box is smaller than the second one")
    else:
        print("Boxes are incomparable")
