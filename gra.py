def initial_word_formation():
    while True:

        print("\n\nPodaj słowo które będzie trzeba odgadnąć: \n> ", end='')
        slowo = input()
        if slowo == '':
            print("Podaj poprawna wartosc!")
            continue
        slowo = list(slowo.upper())
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        return slowo

def drawing_hang_station(zycia):
    match zycia:
        case 10:
            pass
        case 9:
            print('\n\n\n\n\n\n ______')
        case 8:
            print('\n|\n|\n|\n|\n|\n|______')
        case 7:
            print(' _____\n|\n|\n|\n|\n|\n|______')
        case 6:
            print(' _____\n|    |\n|\n|\n|\n|\n|______')
        case 5:
            print(' _____\n|    |\n|    0\n|\n|\n|\n|______')
        case 4:
            print(' _____\n|    |\n|    0\n|    |\n|\n|\n|______')
        case 3:
            print(' _____\n|    |\n|    0\n|   /|\n|\n|\n|______')
        case 2:
            print(' _____\n|    |\n|    0\n|   /|\ \n|\n|\n|______')
        case 1:
            print(' _____\n|    |\n|    0\n|   /|\ \n|  _/\n|\n|______')
        case 0:
            print(' _____\n|    |\n|    0\n|   /|\ \n|  _/ \_ \n|\n|______')
        case _:
            print('')

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
        zdrapka_check = zdrapka.copy()

        for i in range(dlugosc_slowa):
            if (slowo[i] == literka):
                zdrapka[i] = literka
        if (zdrapka_check == zdrapka):
            zycia -= 1
        if(slowo == zdrapka):
            print("Wygrałeś!")
            break
        drawing_hang_station(zycia)
        print(' '.join(zdrapka))
        if(zycia == 0):
            print('Przegrałeś!')


def gameplay():
    while True:
        slowo = initial_word_formation()
        life_check(slowo)
        break

gameplay()
#3001447

#dodać wykluczanie spacji
#dodać randomowe słowa i wybór trybu gry