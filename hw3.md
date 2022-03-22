CSE1017 프로그래밍기초 (2022) 
숙제 3 [2점] 
마감 :  1반 3월 31일, 2반 4월 5일; 수업시작 직전까지 코드파일 문제별 업로드

### 문제 3.1 : 쌍둥이 찾기 [0.6점]

인수를 3개 받아서 인수를 서로 비교하여
- 3개가 모두 같은 경우, 같은 인수를 `n` 이라고 할 때, `(n, "triple")`을 리턴하고,
- 2개만 같은 경우, 같은 인수가 `n` 이라고 할 때, `(n, "twin")`을 리턴하고,
- 같은 인수가 없으면 `None`을 리턴하는
함수 `identical`을 작성하자.

```
def identical(x,y,z):
    pass

# Test code
print(identical(2,3,4)) # None
print(identical(2,2,4)) # (2, "twin")
print(identical(2,3,2)) # (2, "twin")
print(identical(2,3,3)) # (3, "twin")
print(identical(3,3,3)) # (3, "triple")
```


### 문제 3.2 부동소수점수도 확인할 수 있도록 `isfloat` 함수 확장하기 [0.8점]

실습 3.10에서 작성한 `isfloat` 함수는 정수와 고정소수점 수 문자열만 확인해준다.
부동소수점 수 문자열도 확인할 수 있도록 `isfloat`를 다시 작성하자.
부동소수점 수는 `e`를 가운데 두고, 왼쪽에는 정수 또는 고정소수점 수(음수 포함)를 붙이고,
오른쪽에는 정수(음수 포함)를 붙여서 표현한다.
예를 들면 다음 사례는 모두 합법적인 부동소수점 수 표현 사례이다.
```
>>> 0e3
0.0
>>> 1.3e0
1.3
>>> 0.1e3
100.0
>>> 1e3
1000.0
>>> 1.314e4
13140.0
>>> -1.1e-2
-0.011
>>> .3e4
3000.0
>>> 2.e-2
0.02
```
실제로는 앞에 `+` 기호를 붙여도 상관없으나
이 문제에서는 편의상 `+` 기호는 허용하지 않는 걸로 한다.
이미 작성해둔 다음 `isinteger` 함수는 그대로 호출하여 써도 좋다.
```
def isinteger(s):
    return s.isdigit() or \
           s != '' and s[0] == '-' and s[1:].isdigit()
```
기존에 작성해둔 `isfloat` 함수는 고정소수점 수를 확인해주므로
함수 이름을 다음과 같이 `isfixed`로 바꾸어 그대로 두고 활용하여
`isfloat` 함수를 새로 작성하면 수월해진다.
```
def isfixed(s):
    (num, dot, fraction) = s.partition('.')
	  return dot == '' and fraction == '' and isinteger(num) or \
           dot == '.' and \
           ((num == '' or num == '-') and fraction.isdigit() or \
            fraction == '' and isinteger(num) or \
            isinteger(num) and fraction.isdigit())
```

```
def isfloat(s):
	(significand, e, exponent) = s.partition('e')
    return None # 여기에 논리식을 채워서 완성한다.
```


#### 실행 사례

```
# Test code
print(isfloat("2"))       # True
print(isfloat("-2"))      # True
print(isfloat(".112"))    # True
print(isfloat("-.112"))   # True
print(isfloat("3.14"))    # True
print(isfloat("-3.14"))   # True
print(isfloat("5."))      # True
print(isfloat("5.0"))     # True
print(isfloat("-777.0"))  # True
print(isfloat("-777."))   # True
print(isfloat("."))       # False
print(isfloat(".."))      # False
print(isfloat("0e3"))     # True
print(isfloat("1.3e0"))   # True
print(isfloat("0.1e3"))   # True
print(isfloat("1e3"))     # True
print(isfloat("1.314e4")) # True
print(isfloat("-1.1e-2")) # True
print(isfloat(".3e4"))    # True
print(isfloat("2.e-2"))   # True
print(isfloat("0e3"))     # True
```

### 문제 3.3 [0.6점]

생년월일을 인수로 각각 받아서 성년인지 확인하는 함수 `check_adult`를 작성하자.
만 19살이 되는 생일부터 성년으로 인정한다.
즉, 만 19살 생일이거나 지났으면 `True`를 리턴하고, 그렇지 않으면 `False`를 리턴한다.
파이썬 표준 라리브러리의 `datetime` 모듈의 `date` 객체를 활용하면
오늘 날짜를 다음과 같이 년, 월, 일 별도로 얻을 수 있다.

```
>>> from datetime import date
>>> today = date.today()
>>> today.year
2021
>>> today.month
3
>>> today.day
18
>>>
```
인수는 모두 실제로 존재하는 년, 월, 일이며 정수로 주어진다고 가정해도 좋다.

#### 뼈대 코드
```
from datetime import date

def check_adult(year,month,day):
    from datetime import date
    today = date.today()
    return None # 여기에 논리식을 채워서 작성하자.
```

#### Test code

```
today = date.today()
year = today.year
month = today.month
day = today.day
print(today)
print(check_adult(year-20,12,31))       # True
print(check_adult(year-19,month-1,1))   # True
print(check_adult(year-19,month,day-1)) # True
print(check_adult(year-19,month,day))   # True
print(check_adult(year-19,month,day+1)) # False
print(check_adult(year-19,month+1,1))   # False
```
