ls = [1, 2, 3, 9, 5,18, 2, 0]

pa = []
max1 = ls[0]

def range1(ls):
    largest = ls[0]
    lowest = ls[0]
    largest2 = None
    lowest2 = None
    for i in ls[1:]:
        print("i in for and largest ", i, largest)
        if i > largest:
            largest2 = largest
            print("largest2 : ", largest2)
            largest = i
            print("largest: ", largest)
        elif largest2 == None or largest2 < i:
            largest2 = i
            print("largest2", largest2)
        if i < lowest:
            lowest2 = lowest
            lowest = i
        elif lowest2 == None or lowest2 > i:
            lowest2 = i
    print(largest, largest2, lowest, lowest2)

def larg(ls):
    larg1 = ls[0]
    larg2 = None
    lowest = ls[0]
    lowest2 = None
    for i in ls[1:]:
        if i > larg1:
            larg2 = larg1
            larg1 = i
    print("max value is", larg1,larg2)


sl = None
fsl = ls[0]
for i in range(len(ls) - 1):
    if ls[i] > fsl:
        sl = fsl
        fsl = ls[i]
print(fsl, sl)
larg(ls)
range1(ls)




