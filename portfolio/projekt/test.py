import turtle as t
import time

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
board_centers = [[(-100, 100), (0, 100), (100, 100)],
                 [(-100, 0), (0, 0), (100, 0)],
                 [(-100, -100), (0, -100), (100, -100)]]
if_wait = False

screen = t.Screen()
diego = t.Turtle(visible=False)
diego.speed("fastest")


def index_search(value, array):
    for i, x in enumerate(array):
        if value in x:
            return i, x.index(value)


def print_board():

    diego.penup()
    diego.goto(-150, 50)
    diego.pendown()
    diego.forward(300)
    diego.penup()

    diego.goto(-150, -50)
    diego.pendown()
    diego.forward(300)
    diego.penup()

    diego.goto(-50, 150)
    diego.pendown()
    diego.right(90)
    diego.forward(300)
    diego.penup()

    diego.goto(50, 150)
    diego.pendown()
    diego.forward(300)
    diego.penup()


def get_place_number(x, y):
    global if_wait
    diego.penup()
    diego.goto(x, y)
    # cos tu trzeba zmienic
    min_distance = 1000000

    """trzeba tutaj znalezc najblizsze centrum i jego index w
    'board_centers' i wywolac insert_letter  z pozycja z 'board'"""
    for row in board_centers:
        for cords in row:
            distance = diego.distance(cords)
            if distance < min_distance:
                min_distance = distance
                closest_centre = cords

    # szukam wiersza i kolumny closest centre w board_centres
    position = index_search(closest_centre, board_centers)
    insert_letter("o", position)
    if_wait = True


def is_free(position):
    if board[position[0]][position[1]] == " ":
        return True
    else:
        return False


def check_draw():
    if_draw = True
    for row in board:
        for position in row:
            if position == " ":
                if_draw = False
    return if_draw

def checkForWin():
    if (board[0][0] == board[0][1] == board[0][2] != ' '):
        return True
    elif (board[1][0] == board[1][1] == board[1][2] != ' '):
        return True
    elif (board[2][0] == board[2][1] == board[2][2] != ' '):
        return True
    elif (board[0][0] == board[1][0] == board[2][0] != ' '):
        return True
    elif (board[0][1] == board[1][1] == board[2][1] != ' '):
        return True
    elif (board[0][2] == board[1][2] == board[2][2] != ' '):
        return True
    elif (board[0][2] == board[1][1] == board[2][0] != ' '):
        return True
    elif (board[0][0] == board[1][1] == board[2][2] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if (board[0][0] == board[0][1] == board[0][2] == mark):
        return True
    elif (board[1][0] == board[1][1] == board[1][2] == mark):
        return True
    elif (board[2][0] == board[2][1] == board[2][2] == mark):
        return True
    elif (board[0][0] == board[1][0] == board[2][0] == mark):
        return True
    elif (board[0][1] == board[1][1] == board[2][1] == mark):
        return True
    elif (board[0][2] == board[1][2] == board[2][2] == mark):
        return True
    elif (board[0][2] == board[1][1] == board[2][0] == mark):
        return True
    elif (board[0][0] == board[1][1] == board[2][2] == mark):
        return True
    else:
        return False

'''
def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    else:
        return False
'''

def insert_letter(letter, position):
    if is_free(position):
        board[position[0]][position[1]] = letter
        diego.goto(board_centers[position[0]][position[1]])
        if letter == "o":
            diego.right(90)
            diego.forward(40)
            diego.left(90)
            diego.pendown()
            diego.circle(40)
            diego.penup()
        elif letter == "x":
            diego.right(45)
            diego.forward(40)
            diego.right(180)

            diego.pendown()
            diego.forward(80)
            diego.penup()

            diego.left(135)
            diego.forward(56.5685)
            diego.left(135)

            diego.pendown()
            diego.forward(80)
            diego.penup()

            diego.right(45)
        if (check_draw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'x':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        '''
        if check_win():
            print(f"{check_win()} wins!")
            exit()
        elif check_draw():
            print("Draw!")
            exit()
            '''


def player_move():
    print("listen")
    screen.listen()
    screen.onscreenclick(get_place_number)
    return


def computer_move():
    global if_wait
    best_score = -800
    best_move = [0, 0]
    for x, row in enumerate(board):
        for y, position in enumerate(row):
            if position == " ":
                board[x][y] = "x"
                score = minimax(board, 0, False)
                board[x][y] = " "
                if score > best_score:
                    best_score = score
                    best_move = [x, y]
    insert_letter("x", best_move)
    if_wait = True
    return


def minimax(board, depth, is_maximizing):
    '''
    if check_win() == "x":
        return 1
    elif check_win() == "o":
        return -1
    '''
    if (checkWhichMarkWon("x")):
        return 1
    elif (checkWhichMarkWon("o")):
        return -1
    elif check_draw():
        return 0

    if is_maximizing:
        best_score = -800
        for x, row in enumerate(board):
            for y, position in enumerate(row):
                if position == " ":
                    board[x][y] = "x"
                    score = minimax(board, depth+1, False)
                    board[x][y] = " "
                    if score > best_score:
                        best_score = score
        return best_score
    else:
        best_score = 800
        for x, row in enumerate(board):
            for y, position in enumerate(row):
                if position == " ":
                    board[x][y] = "o"
                    score = minimax(board, depth+1, True)
                    board[x][y] = " "
                    if score < best_score:
                        best_score = score
        return best_score


def waiter():
    global if_wait
    screen.update()
    if_wait = False
    while not if_wait:
        screen.update()
        time.sleep(.1)

    if_wait = False


print_board()

screen.update()

while not checkForWin():
    computer_move()
    player_move()
    waiter()

screen.exitonclick()

#dobra wersja z gui