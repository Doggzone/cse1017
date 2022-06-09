# [문제 1] 거리두기?
# 문자열 xs를 인수로 받아서 인접한 문자가 같은 경우가 하나도 없으면 True를,
# 하나라도 있으면 False를 리턴하는 함수 distanced를 재귀 함수로 작성하자.
# (1) 아래 뼈대 코드 형식에 맞추어 if-else 제어구조를 활용하여 먼저 완성하고,
# (2) 이어서 논리식만으로 다시 작성하자.

# (1)
def distanced(xs):
    if len(xs) > 1:
        if xs[0] == xs[1]:
            return False
        else:
            return distanced(xs[1:])
    else:
        return True

# # (2)
def distanced(xs):
    return len(xs) <= 1 or \
           xs[0] != xs[1] and distanced(xs[1:])
           
    
# # Test code
# print(distanced(""))        # True
# print(distanced("0"))       # True
# print(distanced("00"))      # False
# print(distanced("0122345")) # False
# print(distanced("0123456")) # True

# [문제 2] 만 나이 계산 함수 
# 생년월일을 인수로 년, 월, 일 각각 자연수로 받아서
# 만으로 몇 살인지 알려주는 함수 how_old를 작성하자.
# 태어나는 날부터 만 0살이고, 1년 후 돌이 되는 날 만 1살이 된다.
# 예를 들어, 2002년 9월 15일 생은 2022년 9월 15일에 만 20살이 되고,
# 2021년 4월에는 만 18살이다.
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

def how_old(year,month,day):
    today = date.today()
    age = today.year - year
    if today.month > month or today.month == month and today.day >= day:
        return age
    else:
        return age - 1

# # Test code
# today = date.today()
# year = today.year
# month = today.month
# day = today.day
# print(today)
# print(how_old(year,month,day+1))      # -1
# print(how_old(year,month,day))        # 0
# print(how_old(year-19,month,day-1))   # 19
# print(how_old(year-19,month,day))     # 19
# print(how_old(year-19,month,day+1))   # 18
# print(how_old(year-19,month-1,day-1)) # 19
# print(how_old(year-19,month-1,day+1)) # 19
# print(how_old(year-19,month+1,day-1)) # 18
# print(how_old(year-19,month+1,day+1)) # 18

# [문제 3] 자연수 짝수열 n개의 누적 합
# 자연수 짝수를 증가하는 순으로 누적하여 합하면 다음과 같다.
#                                 2 =  2
#                             4 + 2 =  6
#                         6 + 4 + 2 = 12 
#                     8 + 6 + 4 + 2 = 20
#                10 + 8 + 6 + 4 + 2 = 30
#                                  ...
#  2 x n + ... + 10 + 8 + 6 + 4 + 2 = sigma_even(n)

# 이와 같이 자연수 짝수열 n 개의 누적 합을 계산하는 (1) 재귀 함수 sigma_even을 구현하고,
# 이어서 (2) 꼬리재귀 함수, (3) while 루프 함수로 변환하자.

# (1) 재귀
def sigma_even(n):
    if n > 0:
        return sigma_even(n-1) + n * 2
    else:
        return 0

# # (2) 꼬리재귀
def sigma_even(n):
    def loop(n,acc):
        if n > 0:
            return loop(n-1,acc+n*2)
        else:
            return acc
    return loop(n,0)

# # (3) while 루프
def sigma_even(n):
    acc = 0
    while n > 0:
        acc += n * 2
        n -= 1
    return acc

# # Test code
# print(sigma_even(0)) # 0
# print(sigma_even(1)) # 2
# print(sigma_even(2)) # 6
# print(sigma_even(3)) # 12
# print(sigma_even(4)) # 20
# print(sigma_even(5)) # 30
# print(sigma_even(6)) # 42
# print(sigma_even(7)) # 56

# [문제 4] 차집합 함수
# (1) 리스트로 표현된 두 집합을 인수로 받아서,
# 차집합을 리턴해주는 함수 difference를 아래 뼈대 코드를 채워서 완성하자.
# 인수 리스트에는 중복된 원소가 없다고 가정한다.
# 그리고 리턴하는 리스트에도 중복된 원소가 없어야 한다.

# xs로 재귀
def difference(xs,ys) :
    if xs != []:
        if xs[0] in ys:
            return difference(xs[1:],ys)
        else:
            return [xs[0]] + difference(xs[1:],ys)
    else :
        return []

# ys로 재귀
# 저절로 꼬리재귀 => (1),(2) 모두의 정답...
def difference(xs,ys):
    if ys != []:
        if ys[0] in xs:
            xs.remove(ys[0])
        return difference(xs,ys[1:])
    else:
        return xs

# (2) 작성한 재귀 함수를 꼬리재귀 함수로 변환하자.

def difference(xs,ys) :
    def loop(xs,zs):
        if xs != []:
            if xs[0] not in ys:
                zs.append(xs[0])
            return loop(xs[1:],zs)
        else:
            return zs
    return loop(xs,[])

# (3) 작성한 꼬리재귀 함수를 while 루프로 변환하자.

def difference(xs,ys) :
    zs = []
    while xs != []:
        if xs[0] not in ys:
            zs.append(xs[0])
        xs = xs[1:]
    return zs

def difference(xs,ys):
    while ys != []:
        if ys[0] in xs:
            xs.remove(ys[0])
        ys = ys[1:]
    return xs

# (4) while 루프 대신, for 루프를 사용하여 함수를 재작성하자.

def difference(xs,ys) :
    zs = []
    for x in xs:
        if x not in ys:
            zs.append(x)
    return zs

def difference(xs,ys):
    for y in ys:
        if y in xs:
            xs.remove(y)
    return xs

# # Test code    
# print(difference([],[]))           # []
# print(difference([1,2],[]))        # [1, 2]
# print(difference([],[3,4]))        # []
# print(difference([1,2],[3,4]))     # [1, 2]
# print(difference([1,2],[2,3]))     # [1]
# print(difference([1,2],[2,1]))     # []
# print(difference([1,2,3],[3,2,1])) # []
# print(difference([1,2,3],[3,2,4])) # [1]
# print(difference([1,2,3],[4,5,6])) # [1, 2, 3]

# [문제 5] 리스트의 선두에서 연속 동일 원소 모두 리스트로 모으기

# (1) 리스트 xs를 인수로 받아서 선두 부분에서 같은 원소로 이어지는 부분만 리스트로 리턴하는
#     함수 head_equiv를 아래 뼈대코드 틀에 맞춰 재귀로 작성하자.
#     재귀 알고리즘은 다음과 같다.
#     - 원소가 하나만 있는 경우에는 그대로 리턴한다.
#     - 원소가 둘 이상 있는 경우, 선두 원소와 바로 다음 원소를 비교하여
#     - 다르면 선두 원소만만으로 구성한 리스트를 리턴한다.
#     - 같으면 선두원소를 후미리스트로 재귀 호출한 결과와 이어붙여서 리턴한다. 

def head_equiv(xs):
    if len(xs) > 1:
        if xs[0] != xs[1]:
            return [xs[0]]
        else:
            return [xs[0]] + head_equiv(xs[1:])
    else:
        return xs

# (2) 작성한 재귀 함수를 꼬리재귀 함수로 재작성하자.

def head_equiv(xs):
    def loop(xs,zs):
        if len(xs) > 1:
            zs.append(xs[0])
            if xs[0] != xs[1]:
                return zs
            else:
                return loop(xs[1:],zs)
        else:
            return zs + xs
    return loop(xs,[])

# (3) 작성한 꼬리재귀 함수를 while 루프를 이용한 함수로 재작성하자.

def head_equiv(xs):
    zs = []
    while len(xs) > 1:
        zs.append(xs[0])
        if xs[0] != xs[1]:
            return zs
        else:
            xs = xs[1:]
    return zs + xs

# # Test code
# print(head_equiv([]))          # []
# print(head_equiv([2]))         # [2]
# print(head_equiv([2,3]))       # [2]
# print(head_equiv([2,2]))       # [2,2]
# print(head_equiv([2,2,2]))     # [2,2,2]
# print(head_equiv([2,2,2,3,3])) # [2,2,2]