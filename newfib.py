
fibonacci_cache = {}


def fn(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    elif n == 1:
        result = 0
    elif n == 2:
        result = 1
    else:
        result = fn(n - 1) + fn(n - 2)

    fibonacci_cache[n] = result
    return result


num = int(input("Enter a number: "))

if num > 0:
    result = fn(num)
    print(f"fn({num}) = {result}")
else:
    print("Error in input")
