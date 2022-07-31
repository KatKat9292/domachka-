def fib(array: int) -> int:
    fib1, fib2 = 1, 1
    for _ in range(array):
        print(fib2, end=' ')
        fib1,fib2 = fib2, fib1 + fib2

fib(6)
