from random import randint
print('podaj rozmiar planszy:')

game_size=int(input())
field=[]
for i in range(game_size):
    field.append(['*'] * game_size)


apple_x=randint(0, game_size-1)
apple_y=randint(0, game_size-1)

player_x=randint(0, game_size-1)
player_y=randint(0, game_size-1)

field[player_x][player_y]='P'
field[apple_x][apple_y]='O'




player_found_apple = False

while not player_found_apple:
    print("poruszasz się za pomocą W/A/S/D, q kończy grę")
    for area in field:
        print(area)
    move=input("dokąd idziesz?")
    match move.upper():
        case 'W':
            field[player_x][player_y] = "*"
            player_x-=1
            field[player_x][player_y] = 'P'
            if player_x<0:
                print('uderzasz w ścianę')

        case 'A':
            field[player_x][player_y] = "*"
            player_y-= 1
            field[player_x][player_y] = 'P'
            if player_y<0:
                print('uderzasz w ścianę')

        case 'S':
            field[player_x][player_y] = "*"
            player_x+=1
            field[player_x][player_y] = 'P'
            if player_x<0:
                print('uderzasz w scianę')

        case 'D':
            field[player_x][player_y] = "*"
            player_y += 1
            field[player_x][player_y] = 'P'
            if player_y < 0:
                print('uderzasz w ścianę')

        case 'Q':
            print("koniec gry")
            quit()
        case '_':
            print("używaj tylko WSAD")



    if player_x==apple_x and player_y==apple_y:
        player_found_apple=True
        print('znalazłeś jabłko jee')
