def spam(number):
    i = 0
    x = ''
    while i <= number - 1:
        x = x + 'bulochka'
        i+=1
    return x



def my_sum(list_of_numbers):

    pass
    x = 0
    for num in list_of_numbers:
        x = x + num
    return x


def shortener(string):
    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     функция должна вместо всех символов после шестого поставить одну звездочку.
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'


    """
    pass
    z = ''
    x = string.split()
    for elem in enumerate(x):
        if len(elem[1]) > 6:
            y = elem[1][:6] + '*'
            x[elem[0]] = y
    for el in x:
        z = z + ' ' + el
    return z.strip()


def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    x = 0
    for elem in words:
        if len(elem) >= 2 and elem[0] == elem[-1]:
            x += 1
    return x