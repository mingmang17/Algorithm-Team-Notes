from collections import deque

#큐(queue) 구현을 위해 deque라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() #왼쪽에서 꺼낸다. # 2 3 7
queue.append(1) # 2 3 7 1
queue.append(4) # 2 3 7 1 4
queue.popleft() # 3 7 1 4

print(queue) #먼저 들어온 순서대로 출력
queue.reverse() #역순으로 바꾸기
print(queue)