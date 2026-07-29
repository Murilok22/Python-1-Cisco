my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my2_list = []

for number in my_list:
    if number not in my2_list:
        my2_list.append(number)
 
print(my2_list)