# 알파코드(DFS)
# 철수와 영희는 암호화 편지 주고 받는다
# 영희 : 알파벳 A:1, B:1, ..., Z=26을 할당하여 번호로 보내자
# 철수 : BEAN이 25114 일 경우는 BEAAD, YAAD, TAN, TKD 등 많다
# 얼마나 많은 방법이 있는지 구해라

# 입력
# 암호롸된 코드가 입력된다. 0이 입력되면 입력 종료를 의미한다.

# 출력
# 입력된 코드를 알파벳으로 복원하는데 몇가지 방법이 잇는지 각 경우를 출력한다. 그 가지수도 출력한다.
# 단어의 출력은 사전순으로 출력한다.

def dfs(L, P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P):
            print(chr(res[j]+64), end='')
        print()
    else:
        for i in range(1, 27): #알파벳 1부터 26까지
            if code[L]==i: #한자리 수일때
                res[P]=i
                dfs(L+1, P+1) #한자리 수니까 +!
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
                res[P]=i
                dfs(L+2, P+1)


code=list(map(int, input()))
n=len(code)
code.insert(n, -1) # 맨 마지막에 왔을 때 2자리수를 검사하면 out of index 에러 발생
res=[0]*(n+3)
cnt=0
dfs(0,0)
print(cnt)
