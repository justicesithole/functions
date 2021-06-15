#Recursion

def binary_search(a_list, item, count):
    print("\n", a_list, "plus count", count)
    count += 1
    if len(a_list) == 0:
        return False

    else:
        midpoint = len(a_list)//2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search(a_list[:midpoint], item, count)
        else:
            return binary_search(a_list[(midpoint + 1):], item, count)

my_list = [x for x in range(0, 100) if x%2 == 0]
print(my_list)

print(binary_search(my_list, 2, 0))
print(binary_search(my_list, 3, 0))
