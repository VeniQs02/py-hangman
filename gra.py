def gameplay():
    while True:
        print("\n\nPodaj słowo które będzie trzeba odgadnąć: \n> ", end='')
        slowo = list(input())
        if slowo == '':
            continue
        dlugosc_slowa = len(slowo)
        print(slowo)
        print('_ ' * dlugosc_slowa)

        while True:
            input("Podaj literkę: ")
            if(sprawdzanie_literek == 'h'):
                print('cokolwiek')





gameplay()
