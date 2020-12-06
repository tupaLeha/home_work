ivanov_list = [95, 75, 80]
petrov_list = [80, 80, 92]
sidorov_list = [75,60, 81]
golovach_list = [80, 86, 85]
academic_avarage = {}
academic_performance = {
    'Ivanov Andrey': ivanov_list,
    'Petrov Anton': petrov_list,
    'Sidorov Petro': sidorov_list,
    'Golovach Lena': golovach_list,
}
x = list(academic_performance.values())
def avarage(list):
    z = sum(list)/len(list)+1
    return int(z)
ivanov_avarage = avarage(x[0])
petrov_avarage = avarage(x[1])
sidorov_avarage = avarage(x[2])
golovach_avarage = avarage(x[3])
def avarage_max(list):
    a = [ivanov_avarage, petrov_avarage, sidorov_avarage, golovach_avarage]
    return max(a)
print(avarage_max(x))
def avarage_min(list):
    b = [ivanov_avarage, petrov_avarage, sidorov_avarage, golovach_avarage]
    return min(b)
print(avarage_min(x))
academic_avarage['Ivanov Andrey'] = ivanov_avarage
academic_avarage['Petrov Anton'] = petrov_avarage
academic_avarage['Sidorov Petro'] = sidorov_avarage
academic_avarage['Golovach Lena'] = golovach_avarage
print(academic_avarage)