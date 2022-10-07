
def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow%i==0:
            yellow_w=yellow//i
            yellow_h=i
            if brown==(yellow_w*2+yellow_h*2+4):
                brown_w=yellow_w+2
                brown_h=yellow_h+2
                if brown_w<brown_h:
                    swap=brown_w
                    brown_w=brown_h
                    brown_h=swap
        
    
    answer = [brown_w, brown_h]
    return answer
