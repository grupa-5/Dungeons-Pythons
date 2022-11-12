from random import randint

field_area = int(input("Podaj rozmiar planszy: "))
field = []
for i in range(field_area):
    field.append(['*'] * field_area)

player_x = 0
player_y = 0
apple_x = 0
apple_y = 0
wall = "Ściana!!!! Wybierz inny kierunek"

while player_x == apple_x and player_y == apple_y:
    player_x = randint(0, field_area - 1)
    player_y = randint(0, field_area - 1)
    apple_x = randint(0, field_area - 1)
    apple_y = randint(0, field_area - 1)

field[player_x][player_y] = 'P'
field[apple_x][apple_y] = 'O'


while player_x != (apple_x) or player_y != (apple_y):
    for area in field:
        print(area)
    move = input("Gdzie chcesz iść: (WSAD)").upper()

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
        case _:
            print("Zła komenda!!!! Wpisz jeszcze raz!!!!")

print("Znalazłeś jabłko!! Koniec Gry!!")

