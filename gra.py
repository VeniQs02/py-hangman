def initial_word_formation():
    while True:
        print("\n\nPodaj słowo które będzie trzeba odgadnąć: \n> ", end='')
        slowo = input().upper()
        if slowo == '':
            print("Podaj poprawna wartosc!")
            continue
        slowo = list(slowo)
        # print(slowo)
        return slowo

def life_check(slowo):
    zdrapka = []
    dlugosc_slowa = len(slowo)
    for i in range(dlugosc_slowa):
        zdrapka.append('_')
    print(' '.join(zdrapka))
    zycia = 10
    while zycia > 0:
        literka = input("Podaj literkę: ").upper()
        if (literka == ''):
            print("Podaj poprawna wartosc!")
            continue
        print(f"Literka to: {literka}")
        zdrapka_check = zdrapka
        for i in range(dlugosc_slowa):
            if (slowo[i] == literka):
                zdrapka[i] = literka
            if (zdrapka_check == zdrapka):
                zycia -= 1
        print(' '.join(zdrapka))

def gameplay():
    while True:
        slowo = initial_word_formation()
        life_check(slowo)

gameplay()
