def solution(A):
    # write your code in Python 2.7
    argsort = sorted(range(len(A)), key=A.__getitem__)
    midx_pos = argsort[-3:]
    mval_pos = [A[id] for id in midx_pos]
    midx_neg = argsort[:2] + argsort[-1:]
    mval_neg = [A[id] for id in midx_neg]
    product_pos = 1
    product_neg = 1
    for i in range(3):
        product_pos *= mval_pos[i]
        product_neg *= mval_neg[i]
        
    return max(product_pos, product_neg)
