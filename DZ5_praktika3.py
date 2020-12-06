f = open('text.txt', 'r')
x = f.read().split()
S = {}
def word_counter(word):
    if word in S:
        S[word] +=1
    else:
        S[word] = 1

list(map(word_counter, x))
print(S)
