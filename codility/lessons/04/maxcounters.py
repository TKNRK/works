def solution(N, A):
    # write your code in Python 2.
    M = len(A)
    counters = [0 for _ in range(N)]
    bases = [0 for _ in range(N)]
    current_base = 0
    current_max = 0
    for i in range(M):
        elm = A[i]
        idx = elm - 1
        if idx == N:
            current_base = current_max
        else:
            # if idx[th] base is smaller than current base, update its counter and base 
            if bases[idx] < current_base:
                counters[idx] = current_base
                bases[idx] = current_base
            # update its counter
            counters[idx] += 1
            # update current max counter
            current_max = max(current_max, counters[idx])

    # update all counters referencing the bases
    for i in range(N):
        if bases[i] < current_base:
            counters[i] = current_base
    
    return counters