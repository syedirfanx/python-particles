names = ['Amir', 'Karim', 'Jamil', 'Sakir']

index = 0

for name in names:
    print(index, name)
    index += 1


# Good Practise

for index, name in enumerate(names, start=1):
    print(index, name)
