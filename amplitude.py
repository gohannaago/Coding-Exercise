#%%
def solution(A, K):
    # sort the list A
    A = sorted(A)
    print(A)
    # search all the possibilities with window size len(A)-K
    min_amp = A[-1] - A[0] #initialize amplitude
    for i in range(K+1):
        print("Print window:", A[i:i+len(A)-K])
        if (A[i+len(A)-K-1] - A[i]) < min_amp:
            min_amp = A[i+len(A)-K-1] - A[i]
    
    return min_amp
# %%
