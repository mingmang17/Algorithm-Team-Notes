n , m = map(int,input().split())
data = list(map(int, input().split()))

array = [0]*(m+1)

for x in data:
    array[x] += 1

result = 0
for i in range(1, m+1):
    n -=array[i] #무게가 i인 볼링공의 개수(a가 선택할수 있는 개수)제외
    result += array[i] * n #n : b가 선택할수 있는 개수

print(result)
