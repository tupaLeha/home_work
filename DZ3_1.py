import sys
filename = sys.argv[0]
f = open(filename, 'r')
for line in f:
    print(''.join(reversed(line)))
f.close()