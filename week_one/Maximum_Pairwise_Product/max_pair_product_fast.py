def max_pair(a , n):
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
    return result

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    print(max_pair(a, n))
