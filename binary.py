#%%
def solution(A, B):
    # write your code in Python 3.6
    C = A * B #C is an integer as well
    n = C # make a copy for division

    # create empty list to collect binaries
    bin_array = []

    while n > 0:
        bin_array.append(n%2) #append either 0 or 1
        n = n//2 #integer division

    # # join list of strings into single string and convert to integer
    # binary_num = ''.join([str(num) for num in bin_array]) 
    # binary_num = int(binary_num)

    binary_count = sum(bin_array)

    return binary_count



#%%