def solution(A):
    # write your code in Python 2.7
    A.sort()
    if len(A) < 3:
        return 0
    else:
        flag = 0
        for i in range(len(A) - 2):
            fst = A[i]
            scd = A[i+1]
            trd = A[i+2]
            if trd < fst + scd:
                flag = 1    
                break
        return flag
