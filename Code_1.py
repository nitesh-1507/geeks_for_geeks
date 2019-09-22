# program to insert 5 to make the number largest
num = -817

if num > 0:
    if str(num)[0] < '5':
        print('5' + str(num))
    else:
        c = 0
        for i in str(num):
            if i > '5':
                c = c + 1
            else:
                break
        print(str(num)[0:c] + '5' + str(num)[c:len(str(num))])
elif num == 0:
    print('5' + '0')
else:
    if str(abs(num))[0] > '5':
        print('-' + '5' + str(abs(num)))
    else:
        d = 0
        for i in str(abs(num)):
            if i < '5':
                d = d + 1
            else:
                break
        print('-' + str(abs(num))[0:d] + '5' + str(abs(num))[d:len(str(abs(num)))])

