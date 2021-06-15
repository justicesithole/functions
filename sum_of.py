#Sum of

def sum_of(num):
    if num <= 1:
        return 0
    else:
        return num + sum_of(num - 2)

print(sum_of(4))
print(sum_of(6))
print(sum_of(10))
