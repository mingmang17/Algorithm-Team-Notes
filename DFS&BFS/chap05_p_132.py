#재귀함수

#반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

#재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: #n이 1이하인경우 1을 반환(수학적으로 0!과 1!의 값은 1이다.)
        return 1
    return n * factorial_recursive(n-1) # n * (n-1)!

# 각각의 방식으로 구현한 n! 출력 (n=5)
print('반복적으로 구현:' ,factorial_iterative(5))
print('재귀적으로 구현:' ,factorial_recursive(5))
