from collections import deque

def solution(H):
    base = deque([0])
    blocks = 0
    for h in H:
        if base[-1] < h:
            base.append(h)
            blocks += 1
        else:
            while(True):
                try:
                    if base[-1] > h:
                        base.pop()
                    else:
                        break
                except:
                    break
            if base[-1] < h:
                blocks += 1
                base.append(h)
    
    return blocks
