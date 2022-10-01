# 2부터 n-1까지 나누기
# 2부터 n-1까지의 수 모두를 확인하기 때문에, 시간 복잡도가 O(n)
# 시간 초과
def isprime1(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True
 
# n/2까지 나누기
# 여전히 시간 복잡도가 O(n)
# 시간초과
def isprime2(n):
    for i in range(2, n//2+1):
        if n%i==0:
            return False
    return True

# n의 제곱근까지 확인
# 시간복잡도는 O(root n)
def isprime3(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if isprime3(i):
            answer+=1           
    return answer
  
  
# 에라토스테네스체

def solution(n):
    answer = 0
    ch=[0]*(n+1)
    cnt=0
    for i in range(2, n+1):
        if ch[i]==0:
            cnt+=1
            for j in range(i, n+1, i):
                ch[j]=1
    answer=cnt          
    return answer
  
