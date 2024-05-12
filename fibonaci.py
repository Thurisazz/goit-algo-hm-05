def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n not in cache:
            if n <= 1:
                return n
        else:
            cache[n] = n 
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib(0))
print(fib(1))

