def list_sum(a_list, count):
    count += 1
    if len(a_list)== 1:
        return a_list[0]
    else:
        print("\n", a_list, "plus count", count)
        return a_list[0] + list_sum(a_list[1:], count)

my_list = [x for x in range(0, 100) if x%2 == 0]
print(my_list)
print(list_sum(my_list, 0))

