def quantity(list1, elem, max1):
    if elem < len(list1):
        if list1[elem] > max1:
            max1 = list1[elem]
        return quantity(list1, elem + 1, max1)
    else:
        return max1


def quantity2(list1, elem, maxx, i):
    if elem < len(list1):
        if list1[elem] == maxx:
            i = i + 1
        return quantity2(list1, elem + 1, maxx, i)
    else:
        return i


list1 = [int(x) for x in input("Введіть список натуральних чисел: ").split()]
print(quantity2(list1, 0, quantity(list1, 0, 0), 0))
