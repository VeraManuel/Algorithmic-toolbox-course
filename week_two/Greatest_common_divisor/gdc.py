def gdc(a, b):
    if b == 0:
        return a
    prime = (a % b)
    return gdc(b, prime)

if __name__ == '__main__':
    n = int(2)
    numbers = [int(x) for x in input().split()]
    a = numbers[0]
    b = numbers[1]
    print(gdc(a, b))