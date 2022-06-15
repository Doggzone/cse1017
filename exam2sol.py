# 학번:
# 이름:

# 문제 1

def create_ox_box(yes,no):
    import random
    random.seed(33)
    o = ["O" for _ in range(yes)]
    x = ["X" for _ in range(no)]
    ballot = o + x
    random.shuffle(ballot)
    return ballot
##print(create_ox_box(15,13))
##print(create_ox_box(13,15))

box0 = ['X', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'X',
        'X', 'X', 'X', 'O', 'O', 'X', 'O', 'X']
box1 = ['X', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'X',
        'O', 'O', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'X',
        'X', 'X', 'X', 'O', 'O', 'X', 'O', 'X']

def show_ballot_box(box):
    counter = 0
    for ballot in box:
        print(ballot, end=' ')
        counter += 1
        if counter % 10 == 0:
            print()
    if counter % 10 != 0:
        print()

def ballot_sorter(box):
    yes = 0
    no = 0
    o_box = []
    x_box = []
    for ballot in box:
        if ballot == "O":
            yes += 1
            o_box.append(ballot)
        else: # ballot == "X"
            no += 1
            x_box.append(ballot)
    print("개표 결과 (정상)")
    print("찬성 =", yes)
    show_ballot_box(o_box)
    print("반대 =", no)
    show_ballot_box(x_box) 

##ballot_sorter(box0)
##ballot_sorter(box1)

# 문제 1 - (1)
# 반대표의 기표수가 반(1/2)에 도달하기 직전까지는 제대로 분류하다가, 
# 그 이후에는 반대표를 모두 찬성표로 분류하는 함수
def ballot_sorter_rig1(box):
    yes = 0
    no = 0
    o_box = []
    x_box = []
    for ballot in box:
        if ballot == "O":
            yes += 1
            o_box.append(ballot)
        else: # ballot == "X"
            if no < len(box) // 2 - 1:
                no += 1
                x_box.append(ballot)
            else:
                yes += 1
                o_box.append("O")
    print("개표 결과 (조작1)")
    print("찬성 =", yes)
    show_ballot_box(o_box)
    print("반대 =", no)
    show_ballot_box(x_box) 

##ballot_sorter_rig1(box0)
##ballot_sorter_rig1(box1)

# 문제 1 - (2)
# 반대표가 n장 나올 때마다, 반대표 1장을 찬성표로 분류하는 함수
def ballot_sorter_rig2(box, n):
    yes = 0
    no = 0
    counter = 0
    o_box = []
    x_box = []
    for ballot in box:
        if ballot == "O":
            yes += 1
            o_box.append(ballot)
        else: # ballot == "X"
            counter += 1
            if counter < n:
                no += 1
                x_box.append(ballot)
            else:
                yes += 1
                o_box.append("O")
                counter = 0
    print("개표 결과 (조작2)")
    print("찬성 =", yes)
    show_ballot_box(o_box)
    print("반대 =", no)
    show_ballot_box(x_box)

##ballot_sorter_rig2(box0,10)
##ballot_sorter_rig2(box1,10)
##ballot_sorter_rig2(box1,5)

# 문제 2
def iso_trapezoid(m,n):
    if m > 0 and n > 0:
        for i in range(n+1):
            for _ in range(n-i):
                print(" ", end="")
            for _ in range(m+i*2):
                print("O", end="")
            for _ in range(n-i):
                print(" ", end="")
            print()
    else:
        print("No isisceles trapezoid to draw.")

##iso_trapezoid(3,5)
##iso_trapezoid(4,2)
##iso_trapezoid(8,5)
##iso_trapezoid(9,3)


# 문제 3 - (1)
def show_go_board(b):
    size = len(b)
    for i in range(size):
        for j in range(size):
            print(b[i][j],end=" ")
        print()

def check_omog(b):
    # 가로 검사 
    for i in range(9):
        for j in range(5):
            if b[i][j] != " " and \
               b[i][j] == b[i][j+1] == b[i][j+2] == b[i][j+3] == b[i][j+4]:
                return True
    # 세로 검사
    for i in range(5):
        for j in range(9):
            if b[i][j] != " " and \
               b[i][j] == b[i+1][j] == b[i+2][j] == b[i+3][j] == b[i+4][j]:
                return True
    # 대각선 \ 검사
    for i in range(5):
        for j in range(5):
            if b[i][j] != " " and \
               b[i][j] == b[i+1][j+1] == b[i+2][j+2] == b[i+3][j+3] == b[i+4][j+4]:
                return True
    # 대각선 / 검사
    for i in range(5):
        for j in range(4,9):
            if b[i][j] != " " and \
               b[i][j] == b[i+1][j-1] == b[i+2][j-2] == b[i+3][j-3] == b[i+4][j-4]:
                return True
    return False

# True b0 ~ b3
b0 = [['O', ' ', 'X', 'O', ' ', ' ', 'X', 'O', 'O'],
      ['X', ' ', ' ', ' ', 'O', ' ', 'X', ' ', 'X'],
      ['X', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X'],
      ['X', ' ', 'O', 'O', ' ', 'X', 'O', 'X', 'O'],
      ['O', 'O', 'O', 'X', ' ', 'X', 'O', 'X', 'O'],
      ['X', 'O', 'O', 'X', 'X', 'X', ' ', 'X', ' '],
      ['O', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O'],
      [' ', 'O', 'X', 'O', 'X', ' ', 'O', 'O', 'X'],
      [' ', 'O', 'X', 'O', ' ', ' ', ' ', ' ', 'O']]

b1 = [['O', 'O', 'O', 'X', ' ', ' ', 'X', ' ', 'X'],
      [' ', ' ', ' ', 'X', 'O', 'O', 'O', ' ', 'X'],
      ['X', 'O', 'O', 'O', 'O', 'X', ' ', 'O', 'O'],
      ['X', 'O', ' ', 'X', 'O', 'O', 'O', ' ', ' '],
      ['X', 'O', 'O', 'X', 'X', ' ', 'X', 'X', 'O'],
      ['X', 'X', ' ', 'O', 'X', 'O', ' ', 'X', 'X'],
      [' ', ' ', ' ', ' ', 'X', 'O', 'X', 'O', 'X'],
      ['O', ' ', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
      ['X', 'O', ' ', ' ', 'X', ' ', 'O', ' ', 'X']]

b2 = [['O', 'X', ' ', 'X', 'O', 'X', 'X', 'O', 'X'],
      [' ', 'O', ' ', 'X', 'O', 'X', ' ', 'O', ' '],
      ['X', 'X', 'X', 'O', 'X', 'O', 'O', 'X', ' '],
      [' ', 'X', 'O', 'X', 'O', 'O', 'O', ' ', 'O'],
      [' ', 'X', 'O', 'X', 'O', ' ', 'X', 'O', 'O'],
      ['O', 'X', ' ', 'X', 'X', 'X', 'X', 'O', 'O'],
      [' ', 'O', 'X', 'O', ' ', ' ', ' ', 'X', ' '],
      ['X', 'O', ' ', ' ', 'X', 'X', ' ', 'O', ' '],
      ['O', 'O', 'O', 'O', ' ', ' ', 'X', 'X', ' ']]

b3 = [['O', 'X', 'O', 'O', ' ', 'X', 'O', ' ', 'O'],
      ['X', 'O', 'O', ' ', ' ', 'X', 'O', 'O', 'X'],
      [' ', 'O', 'O', ' ', ' ', 'X', ' ', 'O', 'X'],
      [' ', ' ', 'O', ' ', ' ', 'X', 'O', 'X', 'O'],
      [' ', ' ', 'X', 'O', 'X', ' ', 'X', 'X', ' '],
      [' ', 'O', 'X', ' ', 'O', 'X', 'O', 'X', 'O'],
      ['O', 'X', 'O', 'O', 'X', 'X', 'O', ' ', 'X'],
      ['X', 'X', 'X', 'O', ' ', 'O', ' ', 'X', 'X'],
      ['X', 'X', ' ', 'O', 'O', ' ', 'O', 'X', 'X']]

# False b4~b7
b4 = [['O', 'X', 'X', ' ', 'O', 'O', ' ', 'O', 'X'],
      ['O', 'O', 'O', ' ', 'X', ' ', ' ', 'X', ' '],
      [' ', 'O', 'X', ' ', ' ', 'O', 'X', 'X', 'O'],
      ['X', ' ', ' ', ' ', 'X', ' ', ' ', 'O', 'X'],
      ['X', 'O', 'X', 'O', 'X', ' ', 'X', ' ', ' '],
      ['O', 'X', 'X', 'X', ' ', 'X', 'O', 'O', 'O'],
      ['X', 'O', 'X', 'O', ' ', 'O', ' ', 'X', 'X'],
      ['O', 'X', ' ', 'O', 'O', ' ', 'X', 'X', ' '],
      [' ', 'O', 'O', ' ', 'X', 'O', 'O', 'X', 'O']]

b5 = [['X', 'O', 'O', ' ', ' ', ' ', 'X', ' ', 'X'],
      ['O', ' ', 'X', 'X', ' ', 'X', 'O', 'X', 'O'],
      [' ', 'X', 'X', 'O', 'O', 'O', 'O', ' ', 'O'],
      [' ', 'X', ' ', 'O', 'O', 'X', 'X', 'O', 'O'],
      [' ', 'O', 'X', 'X', 'X', 'X', 'O', 'X', 'X'],
      ['O', ' ', 'O', ' ', 'O', ' ', 'O', ' ', ' '],
      ['X', 'X', 'X', ' ', 'O', 'O', ' ', ' ', 'O'],
      [' ', 'X', 'X', 'X', 'X', ' ', ' ', 'O', 'X'],
      ['O', 'X', ' ', 'O', 'O', ' ', 'O', 'X', ' ']]

b6 = [['X', 'O', 'X', 'X', 'X', ' ', 'O', 'O', 'O'],
      [' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', 'X'],
      ['O', 'X', 'O', ' ', ' ', 'X', 'X', ' ', 'O'],
      ['O', ' ', 'O', 'X', 'O', ' ', ' ', ' ', ' '],
      ['O', 'O', 'X', ' ', 'O', ' ', 'X', 'X', 'X'],
      ['X', 'O', 'X', ' ', 'X', 'O', ' ', ' ', 'O'],
      ['O', ' ', ' ', 'O', 'O', 'X', 'X', 'X', 'O'],
      ['X', ' ', 'O', 'X', 'X', 'O', 'O', 'X', 'O'],
      ['O', 'X', 'O', ' ', 'O', 'X', ' ', 'X', 'O']]

b7 = [['X', ' ', ' ', 'O', ' ', 'O', 'O', 'X', 'O'],
      ['X', 'O', 'X', 'O', ' ', 'O', 'X', ' ', 'X'],
      ['O', ' ', 'O', ' ', ' ', 'O', 'X', 'X', 'X'],
      ['X', ' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X'],
      ['O', 'O', 'X', 'O', 'X', 'O', ' ', ' ', 'O'],
      ['X', 'O', 'X', 'X', 'O', 'X', ' ', ' ', ' '],
      ['X', 'X', ' ', ' ', ' ', 'O', 'O', 'X', 'O'],
      ['O', 'X', ' ', 'O', 'X', 'O', 'X', ' ', 'O'],
      ['O', 'O', 'O', 'X', ' ', ' ', 'O', 'X', 'X']]

# 문제 3 - (2)
def initialize_board():
    board = [[] for _ in range(9)]
    for i in range(9):
        for _ in range(9):
            board[i].append(" ")
    return board

from random import randrange
def play_omog():
    board = initialize_board()
    turn = "X"
    n = 0
    while n < 81:
        row = randrange(9)
        col = randrange(9)
        if board[row][col] == " ":
            board[row][col] = turn
            n += 1
            if check_omog(board):
                show_go_board(board)
                print(turn, "wins in", n, "tries")
                break
            turn = "X" if turn == "O" else "O"
    if n == 81:
        show_go_board(board)
        print("No winners!")

##play_omog()

