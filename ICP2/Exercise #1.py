

list1 = ["php", "exercises", "backend"]
list2 = []


for i in range(3):

    a = (list1[i], len(list1[i]))
    list2.append(a)
    list2.sort()




print(list2[0])

