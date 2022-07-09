my_list_int_only = [1, 9, 54 , 0.4, -1, 4, -2]

for i in range(1, len(my_list_int_only), 2):
    my_list_int_only[i - 1],  my_list_int_only[i] = my_list_int_only[i], my_list_int_only[i - 1]

print(my_list_int_only)