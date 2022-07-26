str_1 = [1, 2, 3, 4, 5]
list_2 = [str(x) for x in str_1]
print(list_2)
list_2 = int(''.join(list_2))
print(list_2)
print(type(list_2))
list_2 += 1
print(list(str(list_2)))