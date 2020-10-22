import random

# n = int(input())
# a = [int(x) for x in input().split()]

while True:

    n = int(random.randrange(2, 1000))
    x = 0
    a = [int(x)] * n

    for i in range(n):
        a[i] = random.randrange(0, 200000)

    product = 0

    # max pair naive

    for i in range(n):
        for j in range(i + 1, n):
            product = max(product, a[i] * a[j])


    # max pair fast

    index1 = 0
    for i in range(n):
        if a[i] >= a[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0

    for i in range(n):
        if i != index1 and a[i] > a[index2]:
            index2 = i

    result = a[index1] * a[index2]


    if product == result:
        print(n)
        print(a)
        print(product, result)
    else:
        print(n)
        print(a)
        print(index1, index2)
        print('error', product, result)
        quit()
