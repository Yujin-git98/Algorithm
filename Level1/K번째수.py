# 나의 코드
def solution(array, commands):
    new = 0
    answer=[]
    for command in commands:
        #print(command)
        i=command[0]-1
        j=command[1]-1
        k=command[2]-1
        #print(i,j,k)
        new=array[i:j+1]
        new.sort()
        answer.append(new[k])
    return answer

# 참고 코드
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
