# 백준 17208번 오큰수
# 오큰수 : 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수 / 그러한 수 가 없으면 -1
n=int(input()) # 수열 A의 크기
arr=list(map(int, input().split()))
stack=[]
# 오큰수가 없으면 -1을 출력해야 하므로 정답 배열 answer을 -1로 초기화
answer=[-1 for i in range(n)]
for i in range(n):
    # stack이 비어있지 않고, arr[stack 맨위]가 arr[i]보다 작으면 반복
    while stack and arr[stack[-1]] < arr[i]:
        # answer의 stack.pop()한 인덱스 자리에 arr[i]를 넣음
        answer[stack.pop()]=arr[i]
    # stack에 i를 넣음
    stack.append(i)
# 배열을 print할 때 앞에 *을 붙여주면 공백을 기준으로 원소들만 나열됨
print(*answer)
