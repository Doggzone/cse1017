# [문제 1] 홀로?
# 문자열 xs를 인수로 받아서 xs에 두 번이상 나타나는 문자가 하나라도 있으면 False를,
# 그렇지 않으면 True를 리턴하는 함수 solitary를 재귀 함수로 작성하자.
# (1) 아래 뼈대 코드 형식에 맞추어 if-else 제어구조를 활용하여 먼저 완성하고,
# (2) 이어서 논리식만으로 다시 작성하자.

# (1)
def solitary(xs):
    if xs != "":
        if xs[0] in xs[1:]:
            return False
        else:
            return solitary(xs[1:])
    else:
        return True

# # (2)
def solitary(xs):
    return xs == "" or xs[0] not in xs[1:] and solitary(xs[1:])

# # Test code
# print(solitary(""))       # True
# print(solitary("0"))      # True
# print(solitary("0120"))   # False
# print(solitary("012342")) # False
# print(solitary("012345")) # True



# [문제 2] 성인 인증 함수
# 생년월일을 인수로 년, 월, 일 각각 자연수로 받아서
# 성년인지 확인하는 함수 check_adult를 작성하자.
# 만 19살이 되는 생일부터 성년으로 인정한다.
# 즉, 만 19살 생일이거나 지났으면 True를 리턴하고, 그렇지 않으면 False를 리턴한다.
# 파이썬 표준 라리브러리의 datetime 모듈의 date 객체를 활용하면
# 오늘 날짜는 다음과 같이 년, 월, 일 별도로 얻을 수 있다.
# >>> from datetime import date
# >>> today = date.today()
# >>> today.year
# 2021
# >>> today.month
# 3
# >>> today.day
# 18
# >>>
# 인수는 모두 실제로 존재하는 년, 월, 일로만 주어진다고 가정한다.

from datetime import date

def check_adult(year,month,day):
    today = date.today()
    age = today.year - year
    if age > 19:
        return True
    elif age == 19:
        if today.month > month:
            return True
        elif today.month == month and today.day >= day:
            return True
        else:
            return False
    else:
        return False

def check_adult(year,month,day):
    today = date.today()
    age = today.year - year
    return age > 19 or \
           age == 19 and \
           (today.month > month or \
            today.month == month and \
            today.day >= day)


# # Test code
# today = date.today()
# year = today.year
# month = today.month
# day = today.day
# print(today)
# print(check_adult(year-20,12,31))       # True
# print(check_adult(year-19,month-1,1))   # True
# print(check_adult(year-19,month,day-1)) # True
# print(check_adult(year-19,month,day))   # True
# print(check_adult(year-19,month,day+1)) # False
# print(check_adult(year-19,month+1,1))   # False

# [문제 3] 2의 n 승의 누적 합
# 자연수 n 까지의 모든 자연수에 대하여 2의 n 승을 누적하여 합하면 다음과 같다.
#                                  1 =  1
#                              2 + 1 =  3
#                          4 + 2 + 1 =  7 
#                      8 + 4 + 2 + 1 = 15
#                 16 + 8 + 4 + 2 + 1 = 31
#                                   ...
#  (2**n) + ... + 16 + 8 + 4 + 2 + 1 = sigma_power_of_2(n)

# 이와 같이 자연수 2의 n 승의 누적 합을 계산하는 (1) 재귀 함수 sigma_power_of_2를 구현하고,
# 이어서 (2) 꼬리재귀 함수, (3) while 루프 함수로 변환하자.

# (1) 재귀
def sigma_power_of_2(n):
    if n > 0:
        return sigma_power_of_2(n-1) + 2**n
    else:
        return 1

# # (2) 꼬리재귀
def sigma_power_of_2(n):
    def loop(n,acc):
        if n > 0:
            return loop(n-1,acc+2**n)
        else:
            return acc
    return loop(n,1)

# # (3) while 루프
def sigma_power_of_2(n):
    acc = 1
    while n > 0:
        acc += 2**n
        n -= 1
    return acc

# # Test code
# print(sigma_power_of_2(0)) # 1
# print(sigma_power_of_2(1)) # 3
# print(sigma_power_of_2(2)) # 7
# print(sigma_power_of_2(3)) # 15
# print(sigma_power_of_2(4)) # 31
# print(sigma_power_of_2(5)) # 63
# print(sigma_power_of_2(6)) # 127
# print(sigma_power_of_2(7)) # 255

# [문제 4] 합집합 함수
# (1) 리스트로 표현된 두 집합을 인수로 받아서,
#     합집합을 리턴해주는 함수 union을 아래 뼈대 코드를 채워서 완성하자.
#     인수 리스트에는 중복된 원소가 없다고 가정한다.
#     그리고 리턴하는 리스트에도 중복된 원소가 없어야 한다.

def union(xs,ys) :
    if xs != []:
        if xs[0] not in ys:
            return [xs[0]] + union(xs[1:],ys)
        else:
            return union(xs[1:],ys)
    else:
        return ys
    
# (2) 작성한 재귀 함수를 꼬리재귀 함수로 변환하자.

def union(xs,ys) :
    def loop(xs,zs):
        if xs != []:
            if xs[0] not in ys:
                zs.append(xs[0])
            return loop(xs[1:],zs)
        else:
            return zs + ys
    return loop(xs,[])

# (3) 작성한 꼬리재귀 함수를 while 루프로 변환하자.

def union(xs,ys) :
    zs = []
    while xs != []:
        if xs[0] not in ys:
            zs.append(xs[0])
        xs = xs[1:]
    return zs + ys

# (4) while 루프 대신, for 루프를 사용하여 함수를 재작성하자.

def union(xs,ys) :
    zs = []
    for x in xs:
        if x not in ys:
            zs.append(x)
    return zs + ys

def union(xs,ys):
    for i in range(len(ys)):
        if ys[i] not in xs:
            xs.append(ys[i])
    return xs
    
# # Test code    
# print(union([],[]))           # []
# print(union([1,2],[]))        # [1, 2]
# print(union([],[3,4]))        # [3, 4]
# print(union([1,2],[3,4]))     # [1, 2, 3, 4]
# print(union([1,2],[2,3]))     # [1, 2, 3]
# print(union([1,2],[2,1]))     # [2, 1]
# print(union([1,2,3],[3,2,1])) # [3, 2, 1]
# print(union([1,2,3],[3,2,4])) # [1, 3, 2, 4]
# print(union([1,2,3],[4,5,6])) # [1, 2, 3, 4, 5, 6]

# [문제 5] 리스트에서 중복 원소 모두 없애기
# (1) 리스트 xs를 인수로 받아서 중복된 원소를 모두 리스트에서 제거한 리스트를 리턴하는 
#     함수 remove_duplicates를 아래 뼈대코드 틀에 맞춰 재귀로 작성하자.
#     재귀 알고리즘은 다음과 같다.
#     - 선두원소가 후미리스트에 있으면 선두원소를 무시하고 후미리스트로 재귀 호출한 결과를 리턴한다.
#     - 선두원소가 후미리스트에 없으면 선두원소를 히미리스트로 재귀 호출한 결과와 이어붙여서 리턴한다.
#     - 빈 리스트이면 그대로 리턴한다.

def remove_duplicates(xs):
    if xs != []:
        if xs[0] in xs[1:]:
            return remove_duplicates(xs[1:])
        else:
            return [xs[0]] + remove_duplicates(xs[1:]) 
    else:
        return []

# (2) 작성한 재귀 함수를 꼬리재귀 함수로 재작성하자.

def remove_duplicates(xs):
    def loop(xs,zs):
        if xs != []:
            if xs[0] not in xs[1:]:
                zs.append(xs[0])
            return loop(xs[1:],zs) 
        else:
            return zs
    return loop(xs,[])

# (3) 작성한 꼬리재귀 함수를 while 루프를 이용한 함수로 재작성하자.

def remove_duplicates(xs):
    zs = []
    while xs != []:
        if xs[0] not in xs[1:]:
            zs.append(xs[0])
        xs = xs[1:]
    return zs

# # Test code
print(remove_duplicates([3])) # [3]
print(remove_duplicates([3,3,3,3,3])) # [3]
print(remove_duplicates([3,1,3,1,3])) # [1,3]
print(remove_duplicates([1,2,3,4,5])) # [1,2,3,4,5]






