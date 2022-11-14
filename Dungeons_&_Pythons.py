from random import randint

field = []

field_area = int(input("Podaj rozmiar planszy: "))

for i in range(field_area):
    field.append(['*'] * field_area)

while True:
    player_x = randint(0, field_area - 1)
    player_y = randint(0, field_area - 1)
    apple_x = randint(0, field_area - 1)
    apple_y = randint(0, field_area - 1)

    if player_x != apple_x or player_y != apple_y:
        break

field[player_x][player_y] = 'P'
field[apple_x][apple_y] = 'O'
wall = "Ściana!!!! Wybierz inny kierunek"
find_apple = False


while not find_apple:
    for area in field:
        print(area)
    move = input("Gdzie chcesz iść: (WSAD), q aby zakończyć").upper()

    match move:
        case "S":
            if (player_x + 1) >= field_area:
                print(wall)
                continue
            field[player_x][player_y] = "*"
            player_x += 1
            field[player_x][player_y] = "P"
        case "W":
            if (player_x - 1) < 0:
                print(wall)
                continue
            field[player_x][player_y] = "*"
            player_x -= 1
            field[player_x][player_y] = "P"
        case "A":
            if (player_y - 1) < 0:
                print(wall)
                continue
            field[player_x][player_y] = "*"
            player_y -= 1
            field[player_x][player_y] = "P"
        case "D":
            if (player_y + 1) >= field_area:
                print(wall)
                continue
            field[player_x][player_y] = "*"
            player_y += 1
            field[player_x][player_y] = "P"
        case 'Q':
            print("Wyszedłeś z gry")
            quit()
        case _:
            print("Zła komenda!!!! Wpisz jeszcze raz!!!!")

    if player_x == (apple_x) and player_y == (apple_y):
        find_apple = True


print("Znalazłeś jabłko!! Koniec Gry!!")

