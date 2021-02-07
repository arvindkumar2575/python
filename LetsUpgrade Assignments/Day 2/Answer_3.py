list1 = [int(i) for i in input('Enter the number with space : ').split()]
print(list1)
resultlist1 = []
for i in list1:
    if (i % 2) == 0:
        resultlist1.append(i)
print(resultlist1)
