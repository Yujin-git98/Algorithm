from collections import deque
def solution(s):
    list=[]
    for i in s:
        if i=='(':
            list.append(i)
        elif i==')':
            if len(list)==0:
                return False
            else:
                list.pop()

    if len(list)==0:
        return True
    else:
        return False
