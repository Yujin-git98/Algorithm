# 재귀함수로 문제를 풀때 함수이름을 DFS로 설정
def DFS(x):
    if x==0:
        return #함수의 return은 종료의 의미도 있음
    else:
        DFS(x//2) #x를 2로 나눈 몫
				print(x%2, end=' ') # x를 2로 나눈 나머지
        

if __name__=="__main__":
    n=int(input())
    DFS(n)
