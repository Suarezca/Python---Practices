### List compreshion ###


my_origin_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_origin_list)


my_range = range(8)
print( my_range)
print(list(my_range))

my_list = [i for i in range(8)]
print(my_list) 

my_list = [i + 1 for i in range(8)]
print(my_list) 

def sum_five(num):
    return num + 5  

my_list = [sum_five(i) + 1 for i in range(8)]
print(my_list) 