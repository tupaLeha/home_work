fizz = int(input())
buzz = int(input())
fibu = int(input())
i = 1
while i <= fibu:
    if((i % fizz == 0) and (i % buzz == 0)):
        print('FB')
    elif(i % buzz == 0):
        print('B')
    elif(i % fizz == 0):
        print('F')
    else:
        print(i)
    i = i + 1