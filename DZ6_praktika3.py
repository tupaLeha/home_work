size_dict = {
    'XXS' : 'Rus:42, DE:36, USA:8, FR:38, BR:24',
    'XS' : 'RUS:44, DE:38, USA:10, FR:40, BR:26',
    'S' : 'RUS:46, DE:40, USA:12, FR:42, BR:28',
    'M' : 'RUS:48, DE:42, USA:14, FR:44, BR:30',
    'L' : 'RUS:50, DE:44, USA:16, FR:46, BR:32',
    'XL' : 'RUS:52, DE:46, USA:18, FR:48, BR:34',
    'XXL' : 'RUS:54, DE:48, USA:20, FR:50, BR:36',
    'XXXL' : 'RUS:56, DE:50, USA:22, FR:52, BR:38'
}
def size_transmutation(intSize):
    for key,val in size_dict.items():
        if key == intSize:
            return val
print(size_transmutation('XS'))