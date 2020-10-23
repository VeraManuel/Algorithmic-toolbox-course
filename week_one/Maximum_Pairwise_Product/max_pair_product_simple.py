n = int(input())
a = [int(x) for x in input().split()]

sort = sorted(a)
result = sort[n - 1] * sort[n - 2]
print(result)