# CSE1017 프로그래밍기초(2021)
# 기말시험 - 2021.06.16(수)
# 총 35점

# 1. [6점] ASCII 아트

def triangle(n):
    for i in range(1,n+1):
        for _ in range(n-i):
            print(" ", end="")
        for _ in range(2*i-1):
            print(str(i%10), end="")
        print()

def triangle(n):
    for i in range(1,n+1):
        print(" " * (n-i), end="")
        print(str(i%10) * (2*i-1))

# triangle(3)
# triangle(6)
# triangle(13)


# 2. [6점] 퍼트리기

def spread(board):
    n = len(board)
    // board와 똑같은 보드를 clone에 복사
    clone = []
    for i in range(n):
        row = board[i][:]
        clone.append(row)
    // board를 참고하여 clone을 수정
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                if i != 0: clone[i-1][j] = 1
                if i != n-1: clone[i+1][j] = 1
                if j != 0: clone[i][j-1] = 1
                if j != n-1: clone[i][j+1] = 1
    return clone

# spread([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]])
# # [[0,1,0,0],[1,1,1,0],[0,1,0,0],[0,0,0,0]]
# spread([[0,1,0,0],[1,1,1,0],[0,1,0,0],[0,0,0,0]])
# # [[1,1,1,0],[1,1,1,1],[1,1,1,0],[0,1,0,0]]


# 3.[5점] 빈도수 기록 딕셔너리 만들기

def create_frequency_dictionary(s):
    freq_dict = {}
    for element in s:
        if element in freq_dict.keys():
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1
    return freq_dict

# create_frequency_dictionary("hanyangansan")

# 4. [6점] 텍스트 파일 문자 빈도수 Top 5 프린트 하기

def delete_keys(d,key_set):
    for k in key_set:
        if k in d.keys():
            del d[k]
    return d

def show_character_top5(f):
    file = open(f,"r")
    text = file.read()
    char_dict = create_frequency_dictionary(text)
    delete_keys(char_dict, ['\n',' ','.',',',"'"])
    ranked = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(5):
        rank = i + 1
        print(str(rank) + ". ", ranked[i][0], " = ", ranked[i][1], sep="")    
    file.close()

# 5.[6점] 텍스트 파일 문자 빈도수 Top 5 프린트 하기 (계속)

def show_character_top5(f):
    file = open(f,"r")
    text = file.read()
    char_dict = create_frequency_dictionary(text)
    delete_keys(char_dict, ['\n',' ','.',',',"'"])
    ranked = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    print(str(1) + ". ", ranked[0][0], " = ", ranked[0][1], sep="")
    previous = ranked[0][1]
    for i in range(1, 5):
        if ranked[i][1] != previous:
            previous = ranked[i][1]
            rank = i + 1
        print(str(rank) + ". ", ranked[i][0], " = ", ranked[i][1], sep="")    
    file.close()


# 6.[6점] 텍스트 파일 문자 빈도수 Top 5 프린트 하기 (계속)

def show_character_top5(f):
    file = open(f,"r")
    text = file.read()
    char_dict = create_frequency_dictionary(text)
    delete_keys(char_dict, ['\n',' ','.',',',"'"])
    ranked = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    print(str(1) + ". ", ranked[0][0], " = ", ranked[0][1], sep="")
    previous = ranked[0][1]
    for i in range(1, 5):
        if ranked[i][1] != previous:
            previous = ranked[i][1]
            rank = i + 1
        print(str(rank) + ". ", ranked[i][0], " = ", ranked[i][1], sep="")
    n = 5
    while previous == ranked[n][1]:
        print(str(rank) + ". ", ranked[n][0], " = ", ranked[n][1], sep="")
        n += 1
    file.close()

show_character_top5("poem.txt")

##show_character_frequency_ranking_tie_top(10)
