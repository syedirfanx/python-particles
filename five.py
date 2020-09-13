names = ['Amir Khan', 'Karim Benzeam', 'Shahariar Jamil', 'Sakir Mahmud']
heros = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for index, name in enumerate(names):
    hero = heros[index]
    print(f'{name} is {hero} fan')

# Good Practise

for name, hero, universe in zip(names, heros, universes):
    print(f'{name} is {hero} fan from {universe}')


for value in zip(names, heros, universes):
    print(value)
