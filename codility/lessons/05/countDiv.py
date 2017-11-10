def solution(A, B, K):
    # write your code in Python 2.7
    
    if K < A and B < K:
        return 0
    else:    
        left = A / K * K
        right = B / K * K
        
        if right < A:
            return 0
        elif right == A:
            return 1
        else:
            endpoint = right - left
            startpoint = 1
            ans = endpoint / K
            
            if A % K == 0: ans += 1
            
            return ans