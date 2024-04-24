STALA = 'xx_'
napis = '012345678'
shop_list = ['chleb', 'maslo']
person = {
    'imie': 'Jan',
    'nazwisko': 'Kowal',
    'friends': [
        'Adam', 'Piotr'
    ]
}
nothing = None

print(f'Napis + Nic: {STALA}{napis} :: {shop_list[0]} :: {nothing}')
print('Person: ', person['nazwisko'], person['friends'][1], person)
# print(person['zawod'])  # error
# print(person.get('zawod'))  # zwraca None lub X: get('zawod', X)
print(person.get('nazwisko'))
print()
input()

int_value = 10
print('int_value\t', int_value, '\t Typ:', type(int_value), sep='\t\t')
float_from_int = float(12)
print('float_from_int', float_from_int, ' Typ:', type(float_from_int), sep='\t\t')

if 'imie' in person.keys():
    print('if_TAK')
elif 'nazwisko' in person.keys():
    print('elif_tak')
else:
    print('NIE')

# KONSTRUKCJE.PY ###################
print()
for p_name, p_value in person.items():
    print(p_name, p_value)

import konstrukcje
podstawa, objetosc = konstrukcje.prostopadloscian(1, 2, 3)
print(f'Objetosc: {objetosc}')
