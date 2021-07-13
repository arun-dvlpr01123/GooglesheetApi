

my_array = [8, 9, 52, 98, 71, 85, 23, 1, 10, 11, 23, 24]

array_len = len(my_array)

for i in range(0,array_len):
    for j in range(i+1,array_len):
        if my_array[i] <= my_array[j]:
            temp = my_array[i]
            my_array[i] = my_array[j]
            my_array[j] = temp


print(my_array)
