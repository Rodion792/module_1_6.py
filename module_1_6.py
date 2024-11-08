my_dict = {'Artem': 83475643883, 'Lisa': 89493470479, 'Vitaly': 89543012673}
print(my_dict)
print(my_dict['Vitaly'])
print(my_dict.get('Denis'))
my_dict.update({'Sahsa': 8963104632,
                'Alex': 8562205561})
s = my_dict.pop('Vitaly')
print(s)
print(my_dict)

my_set = { 1, 2, 76, 76, 98, 98, 'Alex', 'Denis', 'Denis', True}
print(my_set)
my_set.add((100, 95, 73))
my_set.discard('Alex')
print(my_set)