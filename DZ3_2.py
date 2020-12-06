f = open('num.txt')
lines = f.readlines()
g = open('num1.txt', 'w')
for line in lines:
    x = line.split()
    fizz = int(x[0])
    buzz = int(x[1])
    fibu = int(x[2])
    i = 1
    while i <= fibu:
        if ((i % fizz == 0) and (i % buzz == 0)):
            print('FB')
            g.write('FB')
        elif (i % buzz == 0):
            print('B')
            g.write('B')
        elif (i % fizz == 0):
            print('F')
            g.write('F')
        else:
            print(i)
            g.write(str(i))
        i = i + 1
f.close()
g.close()