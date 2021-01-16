#큰 수의 법칙
# n = 배열의 크기 , m = 숫자가 더해지는 횟수 , k = 연속해서 더할수 있는 횟수

n , m , k = map(int, input().split())
data = list(map(int,input().split()))
data = sorted(data, reverse=True) #내림차순 정렬
first = data[0]
second = data[1]
count =0
#규칙상 (first*k)+second+(first*k)+second...로 더 할수있기 때문에
#가장 큰 수가 더해지는 횟수
count += (m // (k+1))*k
print(count)
count += m % (k+1)

result = 0
result += first*count #가장 큰 수 더하기
result += second*(m-count) # 두번째 수 더하기

print(result)
 
