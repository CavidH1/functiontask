def ferqli_elementler(list1, list2):
    return list(set(list1) ^ set(list2))
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
ferqli_list = ferqli_elementler(list1, list2)
print("Fərqli elementlər:", ferqli_list)
