def get_hit_coordinates():
    coordinates = input("Введите координаты выстрела в диапазоне от A0 до J9: ")
    while len(coordinates) != 2 or not ('A' <= coordinates[0] <= 'J') or int (coordinates[1]) not in range(0,10):
        coordinates = input("Введенные данные не соответствуют требованиям. Введите координаты выстрела в диапазоне от A0 до J9: ")
    return coordinates


def get_ship_coordinates(word):
    coordinates = input(f"Введите координаты {word} в диапазоне от A0 до J9: ")
    while len(coordinates) != 2 or not ('A' <= coordinates[0] <= 'J') or not coordinates[1].isdigit() or int(coordinates[1]) not in range(0,10):
        coordinates = input(f"Введенные данные не соответствуют требованиям. Введите координаты {word} в диапазоне от A0 до J9: ")
    return coordinates


def make_move(matrix, move_column, move_row,  ship_coordinates):
    result = []
    #print("Матрица на входе: ")
    #print_matrix_with_coords(matrix)
    #print(f"Move_row:  {move_row}")
    #print(f"Move_col:  {move_column}")
    #print(f"Ship_coord:  {ship_coordinates}")
    #hit = matrix[move_row][move_column]
    #print(hit)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == move_row and j == move_column:
                if matrix[i][j] == '-':
                    matrix[i][j] = 'O'
                    result.append(True)
                elif matrix[i][j] == '1':
                    is_killed = check_if_ship_killed(move_row, move_column, matrix, ship_coordinates)
                    if is_killed:
                        matrix[i][j] = 'X'
                        result.append(False)
                    else:
                        matrix[i][j] = 'H'
                        result.append(False)
                elif matrix[i][j] == 'H':
                    matrix[i][j] = 'H'
                    result.append(True)
                elif matrix[i][j] == 'X':
                    matrix[i][j] = 'X'
                    result.append(True)
                elif matrix[i][j] == 'O':
                    matrix[i][j] = 'O'
                    result.append(True)
    result.append(matrix)
    #print("Матрица из make_move после добавления удара:")
    print_matrix_with_coords(matrix)
    return result


def create_ships(matrix):
    ships_count = {4: 1, 3: 2, 2: 3, 1: 4}
    ships_coord = []
    for keys in ships_count.keys():
        for j in range(ships_count[keys]):
            value_correct = []
            if not keys == 1:
                value_correct.append(False)
                while not value_correct[0]:
                    start_coordinate = get_ship_coordinates(f'начала {keys}-клеточного корабля №{j + 1}')
                    start_coordinate_col, start_coordinate_row = parse_coordinates(start_coordinate)
                    finish_coordinate = get_ship_coordinates(f'конца {keys}-клеточного корабля №{j + 1}')
                    finish_coordinate_col, finish_coordinate_row = parse_coordinates(finish_coordinate)
                    if abs(start_coordinate_row - finish_coordinate_row) == keys - 1 or abs(start_coordinate_col - finish_coordinate_col) == keys - 1:
                        value_correct[0] = True
                        value_correct[0], matrix, ships_coord_item = cells_ship(matrix, start_coordinate_row, start_coordinate_col, finish_coordinate_row, finish_coordinate_col)
                        ships_coord.append(ships_coord_item)
                        print_matrix_with_coords(matrix)
                    if not value_correct[0]:
                        print('Данные корабля введены некорректно, попробуйте ввести еще раз')
            else:
                value_correct.append(False)
                while not value_correct[0]:
                    start_coordinate = get_ship_coordinates(f'начала и конца {keys}-клеточного корабля №{j + 1}')
                    start_coordinate_col, start_coordinate_row = parse_coordinates(start_coordinate)
                    value_correct[0], matrix, ships_coord_item = cells_ship(matrix, start_coordinate_row, start_coordinate_col,
                                                                            start_coordinate_row, start_coordinate_col)
                    ships_coord.append(ships_coord_item)
                    if not value_correct[0]:
                        print('Данные корабля введены некорректно, попробуйте ввести еще раз')
                    print_matrix_with_coords(matrix)
    return matrix, ships_coord


def create_matrix():
    return [['-' for _ in range(10)] for _ in range(10)]


def print_matrix_with_coords(matrix):
    print("   " + " ".join(str(i) for i in range(10)))
    i = 0
    for row in matrix:
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        letter = letters[i]
        print(f"{letter}  " + " ".join(row))
        i += 1


def parse_coordinates(coord):
    row_letter = coord[0].upper()
    col_number = coord[1]

    col_index = ord(row_letter) - ord('A')
    row_index = int(col_number)

    #print(col_index, row_index)
    return row_index, col_index


def check_if_ship_killed(move_row, move_column, matrix, ship_coordinates):
    intact = []
    hit = []

    for ship in ship_coordinates:
        for row, col in ship:
            cell = matrix[row][col]
            if cell == '1' or cell == 'H':
                intact.append((row, col))
            elif cell == 'X':
                hit.append((row, col))

    if (move_row, move_column) in intact:
        intact.remove((move_row, move_column))
        hit.append((move_row, move_column))

    if intact:
        print(False)
        return False
    elif hit:
        print(True)
        return True


# Обновление карты противника по координате
def enemy_card(matrix_enemy, matrix, number_y, number_x):
    match matrix[number_x][number_y]:
        case '-':
            matrix_enemy[number_x][number_y] = '-'
        case 'X':
            matrix_enemy[number_x][number_y] = 'X'
        case 'H':
            matrix_enemy[number_x][number_y] = 'H'
        case 'O':
            matrix_enemy[number_x][number_y] = 'O'
    #for row in matrix_enemy:
    #    print(row)
    return matrix_enemy


def filling_ship_hor(matrix, number_y_first, number_x_first, number_x_second, coord):
    if number_x_first <= number_x_second:
        for number_x in range(number_x_first, number_x_second + 1):
                matrix[number_y_first][number_x] = '1'
                coord_one_cell = [number_y_first, number_x]
                coord.append(coord_one_cell)
    else:
        for number_x in range(number_x_second, number_x_first + 1):
            matrix[number_y_first][number_x] = '1'
            coord_one_cell = [number_y_first, number_x]
            coord.append(coord_one_cell)
    return matrix


def filling_ship_ver(matrix, number_y_first, number_y_second, number_x_first, coord):
    if number_y_first <= number_y_second:
        for number_y in range(number_y_first, number_y_second + 1):
            matrix[number_y][number_x_first] = '1'
            coord_one_cell = [number_y, number_x_first]
            coord.append(coord_one_cell)
    else:
        for number_y in range(number_y_second, number_y_first + 1):
            matrix[number_y][number_x_first] = '1'
            coord_one_cell = [number_y, number_x_first]
            coord.append(coord_one_cell)
    return matrix


def print_current_points(player_one_points, player_two_points):
    print("\nТекущий счет: ")
    print(f"Игрок 1: {player_one_points}")
    print(f"Игрок 2: {player_two_points}")


def cells_ship(matrix, number_y_first, number_x_first, number_y_second, number_x_second):
    is_correct_coord = True
    coord_lst = []
    start_x = 0
    start_y = 0
    stop_y = 0
    if number_y_first not in range(0, 10) or number_y_second not in range(0, 10) or number_x_first not in range(0, 10) or number_x_second not in range(0, 10):
        is_correct_coord = False
    else:
        if number_y_first == number_y_second:
            cells_count = abs(number_x_first - number_x_second)
            if number_y_first == 0:
                start_y = 0
                stop_y = 2
            elif number_y_first == 9:
                start_y = 8
                stop_y = 10
            else:
                start_y = number_y_first - 1
                stop_y = number_y_first + 2
            if number_x_first <= number_x_second:
                start_x = number_x_first
            else:
                start_x = number_x_second
            counter = 0
            for i in range(start_y, stop_y):
                if not number_x_first == number_x_second:
                    if not (number_x_first == 0 or number_x_second == 9):
                        for j in range(start_x - 1, start_x + cells_count + 2):
                            if matrix[i][j] == '1':
                                counter += 1
                    elif not number_x_first == 0 or number_x_second == 9:
                        for j in range(start_x - 1, start_x + cells_count + 1):
                            if matrix[i][j] == '1':
                                counter += 1
                    else:
                        for j in range(start_x, start_x + cells_count + 2):
                            if matrix[i][j] == '1':
                                counter += 1
                else:
                    if not (number_x_first == 0 or number_x_second == 9):
                        for j in range(start_x - 1, start_x + 2):
                            if matrix[i][j] == '1':
                                counter += 1
                    elif not number_x_first == 0 or number_x_second == 9:
                        for j in range(start_x - 1, start_x + 1):
                            if matrix[i][j] == '1':
                                counter += 1
                    else:
                        for j in range(start_x, start_x + cells_count + 2):
                            if matrix[i][j] == '1':
                                counter += 1
            if counter > 0:
                is_correct_coord = False
            else:
                filling_ship_hor(matrix, number_y_first, number_x_first, number_x_second, coord_lst)
        elif number_x_first == number_x_second:
            cells_count = abs(number_y_first - number_y_second)
            if number_x_first == 0:
                start_x = 0
                stop_x = 2
            elif number_x_first == 9:
                start_x = 8
                stop_x = 10
            else:
                start_x = number_x_first - 1
                stop_x = number_x_first + 2
            if number_y_first <= number_y_second:
                start_y = number_y_first
            else:
                start_y = number_y_second
            counter = 0
            for i in range(start_x, stop_x):
                if not (number_y_first == 0 or number_y_second == 9):
                    for j in range(start_y - 1, start_y + cells_count + 2):
                        if matrix[j][i] == '1':
                            counter += 1
                elif not number_y_first == 0 and number_y_second == 9:
                    for j in range(start_y - 1, start_y + cells_count + 1):
                        if matrix[j][i] == '1':
                            counter += 1
                elif not number_y_second == 9  and number_y_first == 0:
                    for j in range(start_y, start_y + cells_count + 2):
                        if matrix[j][i] == '1':
                            counter += 1
            if counter > 0:
                is_correct_coord = False
            else:
                filling_ship_ver(matrix, number_y_first, number_y_second, number_x_first, coord_lst)


        else:
            is_correct_coord = False
    return is_correct_coord, matrix, coord_lst


player_one_matrix = create_matrix()
player_one_enemy_matrix = create_matrix() # Поле соперника первого игрока

player_two_matrix = create_matrix()
player_two_enemy_matrix = create_matrix() # Поле соперника второго игрока

player_one_points = 0
player_two_points = 0

print("Добро пожаловать в морской бой! "
      "В игре участвуют 2 игрока. Каждому игроку доступна своя карта, на которой игрок располагает корабли, а также карта, на "
      "\nкоторой он видит свои попадания или промахи по кораблям противника. "
      "\nПопадание отмечается на карте соперника знаком Н, промах - знаком О. Если игрок попал по кораблю соперника, "
      "\nза ним остается право следующего хода. Если игрок промахнулся,"
      "\nправо хода переходит к сопернику. Игра продолжается до тех пор, пока все корабли одного из игроков не будут уничтожены."
      "\n ВАЖНО: при размещение кораблей учитывайте, что между кораблями должна быть минимум 1 клетка. Корабль не будте добавлен, если правило не соблюдается. ")

print("Игрок 1\n")
print("Ваше игровое поле: \n")
print_matrix_with_coords(player_one_matrix)

player_one_matrix, player_one_ship_coordinates = create_ships(player_one_matrix)

print("\nИгровое поле вашего соперника: \n")
print_matrix_with_coords(player_one_enemy_matrix)

print("Игрок 2\n")
print("Ваше игровое поле: \n")
print_matrix_with_coords(player_two_matrix)

player_two_matrix, player_two_ship_coordinates = create_ships(player_two_matrix)

print("\nИгровое поле вашего соперника: \n")
print_matrix_with_coords(player_two_enemy_matrix)


is_game_over = False
while is_game_over == False:
    is_turn_player_one = False
    while is_turn_player_one == False and is_game_over == False:
        print("\nИгрок 1\n")
        first_player_hit = get_hit_coordinates()
        hit_row, hit_column = parse_coordinates(first_player_hit)
        #ship_coord = [] # подставить из функции Юры
        move_result = make_move(player_two_matrix, hit_row, hit_column, player_two_ship_coordinates)
        is_turn_player_one = move_result[0]
        player_two_matrix = move_result[1]

        if not is_turn_player_one == True:
            print("Вы поразили соперника\n")
            player_one_points += 1

        player_one_enemy_matrix = enemy_card(player_one_enemy_matrix, player_two_matrix, hit_row, hit_column)

        print("\nИгровое поле вашего соперника: \n")
        print_matrix_with_coords(player_one_enemy_matrix)
        counter = 0
        for row_matrix in range(len(player_two_matrix)):
            for cell_matrix in range(len(player_two_matrix[row_matrix])):
                if player_two_matrix[row_matrix][cell_matrix] == '1':
                    counter += 1
        if counter == 0:
            is_game_over = True
        print_current_points(player_one_points, player_two_points)

    is_turn_player_two = False
    while is_turn_player_two == False and is_game_over == False:
        print("\nИгрок 2\n")
        second_player_hit = get_hit_coordinates()

        hit_row, hit_column = parse_coordinates(second_player_hit)
        #ship_coord = []  # подставить из функции Юры

        move_result = make_move(player_one_matrix, hit_row, hit_column, player_one_ship_coordinates)
        is_turn_player_two = move_result[0]
        player_one_matrix = move_result[1]

        if not is_turn_player_two == True:
            print("Вы поразили соперника\n")
            player_two_points += 1

        player_two_enemy_matrix = enemy_card(player_two_enemy_matrix, player_one_matrix, hit_row, hit_column)

        print("\nИгровое поле вашего соперника: \n")
        print_matrix_with_coords(player_two_enemy_matrix)
        counter = 0
        for row_matrix in range(len(player_one_matrix)):
            for cell_matrix in range(len(player_one_matrix[row_matrix])):
                if player_one_matrix[row_matrix][cell_matrix] == '1':
                    counter += 1
        if counter == 0:
            is_game_over = True
        print_current_points(player_one_points, player_two_points)

print(f'Игра закончена, Вы победили!!!!')