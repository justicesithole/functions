#Integer sum

def int_sum(num):
    if num <= 0:
        return 0
    else:
        return num + int_sum(num - 1)

print(int_sum(12))
print(int_sum(9))
