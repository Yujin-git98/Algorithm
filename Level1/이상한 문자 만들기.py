# 나의 풀이
# 시행착오 : 문자열의 각 단어는 하나 이상의 공백 문자로 구분되어 있음
# 따라서 그냥 s.split()이 아니라 s.split(' ')으로 해야함
def solution(s):
    answer=''
    
    new=s.split(' ')
    for n in new:
        for i in range(len(n)):
            if i%2==0:
                answer+=n[i].upper()
            else:
                answer+=n[i].lower()
        answer+=' '
    answer=answer[:-1]

    return answer
