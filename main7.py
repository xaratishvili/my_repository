def print_pattern(n):
    if n <= 1:
        print(1)
    else:
        result = print_pattern(n - 1)
        for i in range(1, n + 1):
            print(i, end="")
        print()
        return result

print_pattern(10)

