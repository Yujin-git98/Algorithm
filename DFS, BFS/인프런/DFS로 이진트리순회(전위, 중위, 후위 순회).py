# 전위순회 : 부모 -> 왼쪽 -> 오른쪽 : 1 2 4 5 3 6 7
# 중위순회 : 왼쪽 -> 부모 -> 오른쪽 : 4 2 5 1 6 3 7
# 후위순회 : 왼쪽 -> 오른쪽 -> 부모 : 4 5 2 6 7 3 1

#전위순회
def DFS(n):
  if n>7:
    return
  else:
    print(n, end=' ')
    DFS(n*2)
    DFS(n*2+1)
 DFS(1)

#중위순회
def DFS(n):
  if n>7:
    return
  else:
    DFS(n*2)
    print(n, end=' ')
    DFS(n*2+1)
 DFS(1)

#후위순회
def DFS(n):
  if n>7:
    return
  else:
    DFS(n*2)
    DFS(n*2+1)
    print(n, end=' ')
 DFS(1)
