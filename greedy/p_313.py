#문자열 최소한으로 뒤집어서 다 같은수 만들기

data = input()

count0 = 0 #모두 0으로 뒤집는 경우
count1 = 0 #모두 1로 뒤집는 경우
#첫번째 원소 처리
if data[0]==1:
    count0+=1
else:
    count1+=1
#첫번째랑 두번째 원소 비교하면서 시작
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1': #다음 수가 1이면 0으로 바꿔야하니까
            count0+=1
        else: #다음 수가 0이면 1로 바꿔야하니까
            count1+=1

print(min(count0,count1))

