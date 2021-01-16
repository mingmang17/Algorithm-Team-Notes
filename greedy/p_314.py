#만들 수 없는 금액

n = input()
data = list(map(int, input().split()))
data.sort()

target = 1
for i in data:
    #만들 수 없는 금액을 찾았을 때 종료
    #동전보다 만들려는 금액이 크면 만들수 있다.
    #다음 동전이 만들려는 금액보다 크면 만들수 없다.
    if target < i:
        break
    target += i

print(target)
