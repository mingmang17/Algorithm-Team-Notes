#큰 수의 법칙
# n = 배열의 크기 , m = 숫자가 더해지는 횟수 , k = 연속해서 더할수 있는 횟수
n , m , k = map(int, input().split())
data = list(map(int,input().split()))
data = sorted(data, reverse=True) #내림차순 정렬
first = data[0]
second = data[1]

result = 0

while True:
    for i in range(k):
        if m ==0 : break
        result += first
        m -=1 #1번 더할 때 마다 m에서 1씩 빼기
    if m ==0 : break
    result += second
    m -=1
    
print(result)

 
