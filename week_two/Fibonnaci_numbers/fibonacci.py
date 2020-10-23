def fibonacci_number(n):
    first = 0 
    second = 1
    if n <= 1:
        return n
    for i in range(n - 1):
        fibonacci = first + second
        first = second
        second = fibonacci
    
    return fibonacci

if __name__ == "__main__":
    n = int(input())
    print(fibonacci_number(n))