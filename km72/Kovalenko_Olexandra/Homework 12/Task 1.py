def bigger2(list, element, max1, max2):
    if element < len(list):
        if list[element] > max1:
            max2 = max1
            max1 = list[element]
        elif list[element] > max2:
            max2 = list[element]
        return bigger2(list, element + 1, max1, max2)
    else:
        return max2


list1 = [int(x) for x in input("Введіть список натуральних чисел: ").split()]

print(bigger2(list1, 0, 0, 0))
