f = open('num.txt')
lines = f.readlines()
g = open('num1.txt', 'w')
def fizzbuzz(line):
    if line in lines:
        x = line.split()
        fizz = int(x[0])
        buzz = int(x[1])
        fibu = int(x[2])
        i = 1
        while i <= fibu:
            if ((i % fizz == 0) and (i % buzz == 0)):
                g.write('FB')
            elif (i % buzz == 0):
                g.write('B')
            elif (i % fizz == 0):
                g.write('F')
            else:
                g.write(str(i))
            i = i + 1
fizzbuzz_map = list(map(fizzbuzz, lines))
g.close()
f.close()
g = open('num1.txt', 'r')
y = g.readlines()
print(y)