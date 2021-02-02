#유클리드 호제법
#두 자연수 A,B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 한다.
#이 때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
#유클리드 호제법의 아이디어를 재귀함수로 작성할 수 있다.

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(192,162))
