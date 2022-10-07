# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다.
# 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다.
# 연산자는 덧셈, 뺄셈, 곱셈, 나눗셈으로만 이루어져 있다.
# 수와 수 사이에 연산자를 하나씩 넣어서 수식을 하나 만들 수 있다. 이때 주어진 수의 순서를 바꾸면 안된다.
# 우리는 수와 수 사이에 연산자를 하나씩 넣어서 수식을 하나 만들 수 있다. 이때 주어진 수의 순서를 바꾸면 안된다.
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.
# 나눗셈은 정수 나눗셈으로 몫만 취한다.
# 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.

#입력
# 1. 수의 개수 N이 주어진다.
# 2. A1, A2, ..., AN이 주어진다.
# 3. 합이 N-1인 4개의 정수가 주어지는데 차례대로 덧셈, 뺄셈, 곱셈, 나눗셈의 개수이다.

from collections import deque

def dfs(cnt, result, add, sub, mul, div):
    global max_res
    global min_res
    if cnt==N:
        max_res=max(max_res, result)
        min_res=min(min_res, result)
        return
    if add>0:
        dfs(cnt+1, result+num[cnt], add-1, sub, mul, div)
    if sub>0:
        dfs(cnt+1, result-num[cnt], add, sub-1, mul, div)
    if mul>0:
        dfs(cnt+1, result*num[cnt], add, sub, mul-1, div)
    if div>0:
        dfs(cnt+1, -((-result)//num[cnt]) if result<0 else result//num[cnt], add, sub, mul, div-1)

N=int(input())
num=list(map(int, input().split()))
add, sub, mul, div= map(int, input().split())
max_res = -1000000000
min_res = 1000000000
dfs(1, num[0], add, sub, mul, div)
print(max_res)
print(min_res)
