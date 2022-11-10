field_area = int(input("Podaj rozmiar planszy: "))
field = []
for i in range(field_area):
    field.append(['*'] * field_area)

field[0][0] = 'P'
field[field_area - 1][field_area - 1] = 'O'

n = 0
m = 0
wall = "Ściana!!!! Wybierz inny kierunek"
while n != (field_area - 1) or m != (field_area - 1):
    for area in field:
        print(area)
    move = input("Gdzie chcesz iść: (WSAD)").upper()

    match move:
        case "S":
            if (n + 1) >= field_area:
                print(wall)
                continue
            field[n][m] = "*"
            n += 1
            field[n][m] = "P"
        case "W":
            if (n - 1) < 0:
                print(wall)
                continue
            field[n][m] = "*"
            n -= 1
            field[n][m] = "P"
        case "A":
            if (m - 1) < 0:
                print(wall)
                continue
            field[n][m] = "*"
            m -= 1
            field[n][m] = "P"
        case "D":
            if (m + 1) >= field_area:
                print(wall)
                continue
            field[n][m] = "*"
            m += 1
            field[n][m] = "P"
        case _:
            print("Zła komenda!!!! Wpisz jeszcze raz!!!!")

print("Znalazłeś jabłko!! Koniec Gry!!")

