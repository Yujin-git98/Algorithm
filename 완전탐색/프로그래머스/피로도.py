from itertools import permutations
def solution(k, dungeons):
    dun_len=len(dungeons)
    res=0
    for dun in permutations(dungeons, dun_len):
        current=k
        cnt=0
        for i in dun:
        
            if current>=i[0]:
                current-=i[1]
                cnt+=1

        res = max(res, cnt)
    answer=res
    return answer
