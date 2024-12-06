def listim(my_list):
    return len(list(set(my_list)))
my_list = [1, 2, 2, 4, 4, 6, 7, 7]
lokal_list = listim(my_list)
print("lokal deyisenlerin sayi:", lokal_list)