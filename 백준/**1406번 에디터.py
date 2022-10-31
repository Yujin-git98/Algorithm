# 에디터
# 커서는 문장의 맨 앞, 문장의 민 뒤, 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다.
# 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.
# L : 커서를 왼쪽으로 한 칸 옮김(커서가 문장의 맨앞이면 무시됨)
# D : 커서를 오른쪽으로 한 칸 옮김(커서가 문장의 맨뒤이면 무시됨)
# B : 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만,
# 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $ : $라는 문자를 커서 왼쪽에 추가함.
# 초기 편집기에 입력되어 있는 문자열이 주어지고 그 이후 입력한 명령어가 차례로 주어졌을 때,
# 모든 명령어 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오.
# 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치한다.

## 풀이 확인 (PyPy3)
left_stack=list(input()) # 초기 편집기에 입력되어 있는 문자열
#print(s)
m=int(input()) # 입력할 명령어의 개수
right_stack=[]
#oper=[]
for _ in range(m):
    oper=input().split()
    if oper[0]=='P':
        left_stack.append(oper[1])
    elif oper[0]=='L':
        if len(left_stack)!=0:
            right_stack.append(left_stack.pop())
    elif oper[0]=='D':
        if len(right_stack)!=0:
            left_stack.append(right_stack.pop())
    elif oper[0]=='B':
        if left_stack:
            left_stack.pop()
print(''.join(left_stack) +''.join(list(reversed(right_stack))))

## 시간 초과
s=list(input()) # 초기 편집기에 입력되어 있는 문자열
#print(s)
m=int(input()) # 입력할 명령어의 개수
cur=len(s) # 커서는 문장의 맨 뒤에 위치
#oper=[]
for _ in range(m):
    oper=input().split()
    if oper[0]=='P':
        s.insert(cur, oper[1])
        cur+=1
    elif oper[0]=='L':
        if cur!=0:
            cur-=1
    elif oper[0]=='D':
        if cur!=len(s):
            cur+=1
    elif oper[0]=='B':
        if cur!=0:
            cur-=1
            s.pop(cur)
print(''.join(s))
