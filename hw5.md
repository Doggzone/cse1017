CSE1017 프로그래밍기초 (2022) 
숙제 5 [2.1점] 
마감 : 4월 27일 수업시작 직전까지 코드파일 문제별 업로드

### 문제 5.1 : 리스트에서 원소 하나 제거하기 [0.3점]

(1) 리스트 `xs`에서 제일 앞에 위치한 원소 `x` 하나를 제거하여 리턴하는 함수 `remove_one`을 아래 뼈대 코드의 밑줄친 부분을 채워서 완성하자. `x`가 `xs`에 없으면 `xs`를 그대로 리턴한다.

```
def remove_one(x,xs):
    if xs != []:
        if x == xs[0]:
            return ____________________
        else:
            return ____________________
    else:
        return _____

# Test code
print(remove_one(3,[]))        # []
print(remove_one(3,[3]))       # []
print(remove_one(3,[2]))       # [2]
print(remove_one(3,[2,3,2,3])) # [2, 2, 3]
print(remove_one(3,[2,2,2,3])) # [2, 2, 2]
print(remove_one(3,[2,2,2,2])) # [2, 2, 2, 2]
```

(2) 작성한 재귀 함수를 꼬리재귀 함수로 변환하자.

(3) 작성한 꼬리재귀 함수를 `while` 루프로 변환하여 함수 작성을 마무리하자.


### 문제 5.2 : 리스트에서 원소 모두 제거 [0.3점]

(1) 리스트 `xs`에서 원소 `x`를 모두 제거하여 리턴하는 함수 `remove_all`을 아래 뼈대 코드의 밑줄친 부분을 채워서 완성하자. `x`가 `xs`에 없으면 `xs`를 그대로 리턴한다.

```
def remove_all(x,xs):
    if xs != []:
        if x == xs[0]:
            return ____________________________
        else:
            return ____________________________
    else:
        return _____

# Test code
print(remove_all(3,[]))        # []
print(remove_all(3,[3]))       # []
print(remove_all(3,[3,3,3,3])) # []
print(remove_all(3,[2]))       # [2]
print(remove_all(3,[2,3,2,3])) # [2, 2]
print(remove_all(3,[2,2,2,3])) # [2, 2, 2]
print(remove_all(3,[2,2,2,2])) # [2, 2, 2, 2]
```

(2) 작성한 재귀 함수를 꼬리재귀 함수로 변환하자.

(3) 작성한 꼬리재귀 함수를 `while` 루프로 변환하여 함수 작성을 마무리하자.


### 문제 5.3 : 리스트에서 중복 원소 모두 제거하기 [0.3점]

(1) 리스트 `xs`에서 두 번 이상 나타나는 중복 원소를 모두 제거하여 리턴하는 함수 `remove_duplicates`를 앞에서 작성한 `remove_all` 함수를 활용하여 아래 뼈대 코드의 밑줄친 부분을 채워서 완성하자.

```
def remove_duplicates(xs):
    if len(xs) >= 2:
        head = xs[0]
        return ______________________________________________
    else:
        return _____

# Test code    
print(remove_duplicates([]))                  # []
print(remove_duplicates([1]))                 # [1]
print(remove_duplicates([1,1]))               # [1]
print(remove_duplicates([1,1,1,1]))           # [1]
print(remove_duplicates([4,2,3,2,2,4,3,2,1])) # [4, 2, 3, 1]
```

(2) 작성한 재귀 함수를 꼬리재귀 함수로 변환하자.

(3) 작성한 꼬리재귀 함수를 `while` 루프로 변환하여 함수 작성을 마무리하자.


### 문제 5.4 : 합집합 함수 [0.4점]

(1) 리스트로 표현된 두 집합을 인수로 받아서, 합집합을 리턴해주는 함수 `union`을 아래 뼈대 코드의 밑줄친 부분을 채워서 완성하자.
인수 리스트에는 중복된 원소가 없다고 가정한다. 그리고 리턴하는 리스트에도 중복된 원소가 없어야 한다.

```
def union(xs,ys) :
    if xs != []:
        if xs[0] in ys:
            return ____________________
        else:
            return _________________________
    else:
        return ____

# Test code    
print(union([],[]))           # []
print(union([1,2],[]))        # [1, 2]
print(union([],[3,4]))        # [3, 4]
print(union([1,2],[3,4]))     # [1, 2, 3, 4]
print(union([1,2],[2,3]))     # [1, 2, 3]
print(union([1,2],[2,1]))     # [2, 1]
print(union([1,2,3],[3,2,1])) # [3, 2, 1]
print(union([1,2,3],[3,2,4])) # [1, 3, 2, 4]
print(union([1,2,3],[4,5,6])) # [1, 2, 3, 4, 5, 6]
```

(2) 작성한 재귀 함수를 꼬리재귀 함수로 변환하자.

(3) 작성한 꼬리재귀 함수를 `while` 루프로 변환하자.

(4) `while` 루프 대신, `for` 루프를 사용하여 함수를 재작성하자.


### 문제 5.5 : 교집합 함수 [0.4점]

(1) 리스트로 표현된 두 집합을 인수로 받아서, 교집합을 리턴해주는 함수 `intersection`을 아래 뼈대 코드의 밑줄친 부분을 채워서 완성하자.
인수 리스트에는 중복된 원소가 없다고 가정한다. 그리고 리턴하는 리스트에도 중복된 원소가 없어야 한다.

```
def intersection(xs,ys) :
    if xs != []:
        if xs[0] in ys:
            return ______________________________________
        else:
            return ______________________________________
    else:
        return _____

# Test code    
print(intersection([],[]))           # []
print(intersection([1,2],[]))        # []
print(intersection([],[3,4]))        # []
print(intersection([1,2],[3,4]))     # []
print(intersection([1,2],[2,3]))     # [2]
print(intersection([1,2],[2,1]))     # [1, 2]
print(intersection([1,2,3],[3,2,1])) # [1, 2, 3]
print(intersection([1,2,3],[3,2,4])) # [2, 3]
print(intersection([1,2,3],[4,5,6])) # []
```

(2) 작성한 재귀 함수를 꼬리재귀 함수로 변환하자.

(3) 작성한 꼬리재귀 함수를 `while` 루프로 변환하자.

(4) `while` 루프 대신, `for` 루프를 사용하여 함수를 재작성하자.


### 문제 5.6 : 차집합 함수 [0.4점]

(1) 리스트로 표현된 두 집합을 인수로 받아서, 차집합을 리턴해주는 함수 `difference`를 아래 뼈대 코드의 밑줄친 부분을 채워서 완성하자.
인수 리스트에는 중복된 원소가 없다고 가정한다. 그리고 리턴하는 리스트에도 중복된 원소가 없어야 한다.

```
def difference(xs,ys) :
    if xs != []:
        if xs[0] in ys:
            return ______________________________
        else:
            return ______________________________
    else:
        return ____

# Test code    
print(difference([],[]))           # []
print(difference([1,2],[]))        # [1, 2]
print(difference([],[3,4]))        # []
print(difference([1,2],[3,4]))     # [1, 2]
print(difference([1,2],[2,3]))     # [1]
print(difference([1,2],[2,1]))     # []
print(difference([1,2,3],[3,2,1])) # []
print(difference([1,2,3],[3,2,4])) # [1]
print(difference([1,2,3],[4,5,6])) # [1, 2, 3]
```

(2) 작성한 재귀 함수를 꼬리재귀 함수로 변환하자.

(3) 작성한 꼬리재귀 함수를 `while` 루프로 변환하자.

(4) `while` 루프 대신, `for` 루프를 사용하여 함수를 재작성하자.
