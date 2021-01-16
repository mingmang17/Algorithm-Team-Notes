#숫자 카드게임, 각 행마다 작은수를 뽑아 그중에 제일 큰 수 구하기
#n == 행, m == 열
n , m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)