# program to filter even and odd number from list

num = [1,3,4,5,6,7,3]

even_num = [x for x in num if x % 2 == 0]
print(even_num)

odd_num = [x for x in num if x % 2 != 0]
print(odd_num)