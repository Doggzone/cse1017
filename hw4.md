CSE1017 프로그래밍기초 (2022) 
숙제 4 [2점] 
마감 : 4월 13일 수업시작 직전까지 코드파일 문제별 업로드

### 문제 4.1 : 2의 `n` 승의 누적 합

(1) `n` 까지의 모든 자연수에 대하여 2의 `n`승을 누적하여 합하면 다음과 같다.

![p4-2](https://i.imgur.com/QQNr8tL.gif)

이를 계산하는 재귀 함수 `sigma_power_of_2`를 구현하고, 이어서 꼬리재귀 함수, while 루프 함수로 변환하시오.

```
# Test code
print(sigma_power_of_2(0)) # 1
print(sigma_power_of_2(1)) # 3
print(sigma_power_of_2(2)) # 7
print(sigma_power_of_2(3)) # 15
print(sigma_power_of_2(4)) # 31
print(sigma_power_of_2(5)) # 63
print(sigma_power_of_2(6)) # 127
print(sigma_power_of_2(7)) # 255
```

(2) 2의 `n` 승의 누적 합은 다음 프로그램과 같이 덧셈 1번과 거듭제곱 1번, 뺄셈 1번으로 구할 수도 있다.

```
def sigma_power_of_2(n):
    return 2**(n+1) - 1
```

이 함수가 모든 자연수 `n`에 대하여 2의 `n` 승의 누적 합을 맞게 구하는지 수학적 귀납법으로 증명하시오.


### 문제 4.2 : 누적 합

(1) 다음 식과 같이 누적 합을 계산하는 재귀 함수 `sigma_product_power_of_2`를 구현하고, 이어서 꼬리재귀 함수, while 루프 함수로 변환하시오.

![p4-4](https://i.imgur.com/Gy6HWmz.gif)

```
# Test code
print(sigma_product_power_of_2(0)) # 0
print(sigma_product_power_of_2(1)) # 1
print(sigma_product_power_of_2(2)) # 5
print(sigma_product_power_of_2(3)) # 17
print(sigma_product_power_of_2(4)) # 49
print(sigma_product_power_of_2(5)) # 129
print(sigma_product_power_of_2(6)) # 321
print(sigma_product_power_of_2(7)) # 769
```

(2) 위 식의 누적 합은 다음 프로그램과 같이 뺄셈 1번과 거듭제곱 1번, 곱셈 1번, 덧셈 1번으로 구할 수도 있다.

```
def sigma_product_power_of_2(n):
    return (n-1) * 2**n + 1
```

이 함수가 모든 자연수 `n`에 대하여 위 식의 누적 합을 맞게 구하는지 수학적 귀납법으로 증명하시오.
