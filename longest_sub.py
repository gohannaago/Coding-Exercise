#%%
""" 
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
"""

# My intitial approach - takes a lot of memory and time
#  3019 ms, 16 MB
def lengthOfLongestSubstring(self, s: str) -> int:
    # deal exception of empty string
    if len(s) <= 1:
        maxlen = len(s)
    
    # creating dict with substring and its length
    save = {}
    
    # do start and end counter
    start = 0 
    end = start + 1
    a
    # print(s[start:end])
    
    # iterate through s
    while end <= len(s):
        # print("s[end-1]: ", s[end-1])
        # print("s[start:end-1]: ", s[start:end-1])
        
        if s[start:end] not in save and s[end-1] not in s[start:end-1]:
            save[s[start:end]] = end-start
            end += 1   
        elif s[end-1] not in s[start:end-1]:
            end += 1
        else:
            start += 1
            end = start +1
    # print(save)
    
    if len(save) > 0:
        maxlen = max(list(save.values()))
    # return max of values
    return maxlen
        
# Another example of submission
# 40ms

def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_len = 0,0
        used = {}
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
                
            else:
                max_len = max(max_len, i-start+1)
            
            used[s[i]] = i
            
        return max_len

# not save all of the substrings but only the checked char in current sequence
# no need of end counter
# my solution has too many checks in the dict and charcterwise using more time and space

# but why so slow???
        