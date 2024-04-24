
for number in range(1, 15, 3):  # od 1 do 14 co 3
    print(number)

napis = 'abcdx'
for index, letter in enumerate(napis):
    if letter == 'g':
        break
    elif letter == 'h':
        continue
    print(f'{index} -> {letter}')

while True:
    letter = input('Podaj jakas litere ("x" to koniec: ')
    if letter == 'x':
        break
    elif letter == 'h':
        continue
    print(f'Wynik:  {letter}')

def prostopadloscian(bok_a, bok_b, wysokosc=12):
    podstawa = bok_a * bok_b
    objetosc = podstawa * wysokosc
    return podstawa, objetosc

print('Test: ', prostopadloscian(5, 10, 15))