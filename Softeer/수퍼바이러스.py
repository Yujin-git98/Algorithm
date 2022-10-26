# 일부 시간초과
import sys
k, p, n = map(int, sys.stdin.readline().split()) # k : 처음 바이러스의 수, p : 증가율, n : 총 시간
for _ in range(n*10):
    k=k*(n*10)*p
print(k%1000000007)

# 일부 시간 초과
import sys
k, p, n = map(int, sys.stdin.readline().split()) # k : 처음 바이러스의 수, p : 증가율, n : 총 시간
for _ in range(n*10):
    k=(k*p)%1000000007
print(k)

# 풀이 참고
import sys
k, p, n = map(int, sys.stdin.readline().split()) # k : 처음 바이러스의 수, p : 증가율, n : 총 시간
# 시간을 0.1초 단위가 아닌 1초 단위로 생각
n=n*10
mod=1000000007
def pow(n):
    if n<=1:
        return (p**n)%mod
    if n%2==0:
        return (pow(n//2)**2)%mod
    elif n%2==1:
        return (p*pow(n//2)**2)%mod
print((k*pow(n))%mod)

# 풀이 참고 : 재귀
import sys
def pow(n, result):
    if n==1:
        return result
    elif n%2==0:
        a=pow(n/2, result)
        return (a*a)%mod
    else:
        b=pow((n-1)/2, result)
        return (b*b)*result%mod

k, p, n = list(map(int, sys.stdin.readline().split())) # k : 처음 바이러스의 수, p : 증가율, n : 총 시간
# 시간을 0.1초 단위가 아닌 1초 단위로 생각
n=n*10
mod=1000000007
result=pow(n,p)
result*=k
print(result%mod)
