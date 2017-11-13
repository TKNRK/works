def solution1(A):
    return len(set(A))

def solution2(A):
    # write your code in Python 2.7
    N = len(A)
    if N < 1:
        return 0
    else:
        A.sort()
        cnt = 0
        idx = 0
        offset = 0
        try:
            while(True):
                while(A[idx] == A[offset]):
                    offset += 1
                idx = offset
                cnt += 1
        except IndexError:
            pass

        return cnt + 1
