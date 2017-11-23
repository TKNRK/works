from collections import deque

def solution(S):
    # write your code in Python 3.6
    stack = deque()
    flag = 1
    for s in S:
        if s == "(":
            stack.append(s)
        else:
            try:
                stack.pop()
            except:
                flag = 0
                break
    if len(stack) > 0:
        flag = 0
    return flag