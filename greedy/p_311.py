#모험가 길드, 공포도를 이용해 그룹결성, 그룹을 최대한 많이 결성하기

data = list(map(int, input().split()))
#배열을 오름차순으로 정렬하고
data.sort()

result = 0 # 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: #공포도가 제일 낮은 애부터 하나씩 확인하며
    count +=1 #현재 그룹에 해당 모험가를 포함시키기
    if count >=i: #현재 그룹의 모험가의 수가 현재 모험가의 공포도 이상이라면 그룹결성
        result+=1 # 총 그룹수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result)#그룹수 출력

