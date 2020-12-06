num = int(input('Введите желаемую сумму'))
bills = [1000, 500, 200, 100, 50, 20, 10]

for bill in bills:
    x = int(num/bill)
    num = num - bill*x
    print(bill, x)