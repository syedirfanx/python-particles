class Person():
    pass


person = Person()

first_key = 'first_name'
first_value = 'Syed'


setattr(person, first_key, 'Syed')

first_name = getattr(person, first_key)

print(first_name)


person_info = {'first_name': 'Syed', 'last_name': 'Irfan'}

print(person_info['first_name'])

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))
