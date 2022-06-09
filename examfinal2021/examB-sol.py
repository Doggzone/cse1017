# CSE1017 프로그래밍기초(2021)
# 기말시험 - 2021.06.16(수)
# 총 35점

# 1. [7점] ASCII 아트

def rhombus(n):
    for i in range(1,n+1):
        for _ in range(n-i):
            print(" ", end="")
        for _ in range(2*i-1): 
            print(str(i%10), end="")
        print()
    for i in range(n-1,0,-1):
        for _ in range(n-i):
            print(" ", end="")
        for _ in range(2*i-1):
            print(str(i%10), end="")
        print()

def rhombus(n):
    for i in range(1,n+1):
        print(" " * (n-i), end="")
        print(str(i%10) * (2*i-1))
    for i in range(n-1,0,-1):
        print(" " * (n-i), end="")
        print(str(i%10) * (2*i-1))

# rhombus(3)
# rhombus(6)
# rhombus(13)

# 2. [7점] 주위에 있는 지뢰 개수 세어 넣기

def mine_counter(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                if i > 0 and j > 0 and board[i-1][j-1] == "?": board[i][j] += 1
                if i > 0 and board[i-1][j] == "?": board[i][j] += 1
                if i > 0 and j < n-1 and board[i-1][j+1] == "?": board[i][j] += 1
                if j > 0 and board[i][j-1] == "?": board[i][j] += 1
                if j < n-1 and board[i][j+1] == "?": board[i][j] += 1
                if i < n-1 and j > 0 and board[i+1][j-1] == "?": board[i][j] += 1
                if i < n-1 and board[i+1][j] == "?": board[i][j] += 1
                if i < n-1 and j < n-1 and board[i+1][j+1] == "?": board[i][j] += 1
    return board

def print_square(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=' ')
        print()

mine1 = [[0,0,0,0],[0,'?',0,0],[0,0,0,0],[0,0,0,0]]
mine2 = [[0,0,0,0],['?',0,0,0],[0,0,0,0],['?',0,0,0]]
mine3 = [['?','?',0,'?'],[0,0,0,'?'],['?',0,0,0],['?',0,0,'?']]
mine4 = [[0,'?',0,0],['?',0,'?',0],[0,'?',0,0],[0,0,0,'?']]
# print_square(mine_counter(mine1))
# 1 1 1 0 
# 1 ? 1 0 
# 1 1 1 0 
# 0 0 0 0
# print_square(mine_counter(mine2))
# 1 1 0 0 
# ? 1 0 0 
# 2 2 0 0 
# ? 1 0 0
# print_square(mine_counter(mine3))
# ? ? 3 ? 
# 3 3 3 ? 
# ? 2 2 2 
# ? 2 1 ? 
# print_square(mine_counter(mine4))
# 2 ? 2 1 
# ? 4 ? 1 
# 2 ? 3 2 
# 1 1 2 ?

# 3.[7점] 빈자리 채워넣기

def fill_the_gap(ms):
    def loop(ms,ns):
        if ms != []:
            last = ns[len(ns)-1]
            nxt = ms[0]
            if last > nxt:
                while last > nxt:
                    last -= 1
                    ns.append(last)
            elif last < nxt:
                while last < nxt:
                    last += 1
                    ns.append(last)
            else:
                ns.append(nxt)
            return loop(ms[1:],ns)
        else:
            return ns
    if ms != []:
        return loop(ms[1:],[ms[0]])
    else:
        return []
    
# print(fill_the_gap([])) # []
# print(fill_the_gap([3])) # [3]
# print(fill_the_gap([3,3,3])) # [3,3,3]
# print(fill_the_gap([3,2])) # [3,2]
# print(fill_the_gap([3,5])) # [3,4,5]
# print(fill_the_gap([3,6,6,2])) # [3,4,5,6,6,5,4,3,2]
# print(fill_the_gap([9,2,5,4])) # [9,8,7,6,5,4,3,2,3,4,5,4]

# 4. [7점] 16진수를 십진수로 변환하기

def hex2dec(hex):
    length = len(hex)
    dec = 0
    for i in range(length):
        h = hex[i]
        if h in {'1','2','3','4','5','6','7','8','9'}:
            dec += int(h) * 16**(length-i-1)
        elif h == 'A':
            dec += 10 * 16**(length-i-1)
        elif h == 'B':
            dec += 11 * 16**(length-i-1)
        elif h == 'C':
            dec += 12 * 16**(length-i-1)
        elif h == 'D':
            dec += 13 * 16**(length-i-1)
        elif h == 'E':
            dec += 14 * 16**(length-i-1)
        elif h == 'F':
            dec += 15 * 16**(length-i-1)
    return dec

# print(hex2dec("9C4")) # 2500
# print(hex2dec('5B')) # 91
# print(hex2dec('100')) # 256
# print(hex2dec('ACE')) # 2766
# print(hex2dec('DAD')) # 3501
# print(hex2dec('F0F')) # 3855
# print(hex2dec('1024')) # 4132
# print(hex2dec('CC55')) # 52309

# 5.[7점] 십진수를 16진수로 변환하기

def dec2hex(dec):
    hex = ''
    while not (dec == 0):
        r = dec % 16
        if r < 10:
            hex = str(r) + hex
        elif r == 10:
            hex = 'A' + hex
        elif r == 11:
            hex = 'B' + hex
        elif r == 12:
            hex = 'C' + hex
        elif r == 13:
            hex = 'D' + hex
        elif r == 14:
            hex = 'E' + hex
        elif r == 15:
            hex = 'F' + hex
        dec = dec // 16
    return hex

print(dec2hex(2500)) # '9C4'
print(dec2hex(91)) # '5B'
print(dec2hex(256)) # '100'
print(dec2hex(2766)) # 'ACE'
print(dec2hex(3501)) # 'DAD'
print(dec2hex(3855)) # 'F0F'
print(dec2hex(4132)) # '1024'
print(dec2hex(52309)) # 'CC55'