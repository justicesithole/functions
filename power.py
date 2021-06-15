#Integer power


def power(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a * power(a, b - 1)

print(power(3, 4))
print(power(3, 2))
print(power(2, 2))
print(power(2, 1))
print(power(10, 0))
print(power(0, 0))
