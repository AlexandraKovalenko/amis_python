print('Программа счиает пары равных элементов')
while True:
 a =input('Введите список чисел: ').split()
 count = 0
 for i in a:
  for b in a:
   if i == b:
    count=count+1
  count=count-1
 print(int(count/2))
