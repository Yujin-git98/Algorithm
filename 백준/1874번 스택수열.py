# 백준 1874번
n=int(input())

count=1
temp=True
stack=[]
op=[]
# 수열값 입력 받기
for i in range(n):
    # num 이하 숫자까지 스택에 넣기
    num=int(input())
    while count<=num:
        stack.append(count)
        op.append('+')
        count+=1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1]==num:
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp=False
        break

    # 스택 수열을 만들 수 있는지 여부에 따라 출력
    if temp==False:
        print("No")
    else:
        for i in op:
            print(i)
