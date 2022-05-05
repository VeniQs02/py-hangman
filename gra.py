def initial_word_formation():
    while True:
        print("\n\nPodaj słowo które będzie trzeba odgadnąć: \n> ", end='')
        slowo = input().upper()
        if slowo == '':
            print("Podaj poprawna wartosc!")
            continue
        slowo = list(slowo)
        #print(slowo)
        return slowo

def gameplay():
    while True:
        slowo = initial_word_formation()
        zdrapka = []
        dlugosc_slowa = len(slowo)
        for i in range(dlugosc_slowa):
            zdrapka.append('_')
        print(' '.join(zdrapka))
        while True:
            literka = input("Podaj literkę: ").upper()
            if(literka == ''):
                print("Podaj poprawna wartosc!")
                continue
            print(f"Literka to: {literka}")
            for i in range(dlugosc_slowa):
                if(slowo[i] == literka):
                    zdrapka[i] = literka
            print(' '.join(zdrapka))







gameplay()
