students = {
    'ivanov' : {'FrontEnd', 'Python', 'Fullstack'},
    'sidorov' : {'FrontEnd', 'Java'},
    'golovach' : {'Python', 'Fullstack'},
    'vasyn' : {'Java'}
}
def more_then_two(dict):
    x = []
    for key,val in dict.items():
        if len(val) > 1:
            x.append(key)
    return x
print(more_then_two(students))
def not_in_front(dict):
    y = []
    for key,val in dict.items():
        if 'FrontEnd' not in val:
           y.append(key)
    return y
print(not_in_front(students))
def python_and_java(dict):
    z = []
    for key,val in dict.items():
        if 'Python' or 'Java' in val:
            z.append(key)
    return z
print(python_and_java(students))