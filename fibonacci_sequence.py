#Fibonacci sequence

def fib_seq(a_list, max_val):
    if a_list[-1] >= max_val:
        return a_list
    else:
        a_list.append(a_list[-1] + a_list[-2])
        return fib_seq(a_list, max_val)

my_list = [1, 2]

print(fib_seq(my_list, 1000))
