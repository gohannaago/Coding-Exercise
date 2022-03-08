import collections

# Example from leetcode using sliding window

# def characterReplacement(s, k):
#         maxf = i = 0
#         count = collections.Counter()
#         for j in range(len(s)):
#             count[s[j]] += 1
#             maxf = max(maxf, count[s[j]])
#             if j - i + 1 > maxf + k:
#                 count[s[i]] -= 1
#                 i += 1
#         return len(s) - i

#-----------#

# My Implementation
def characterReplacement(s: str, k: int) -> int:
    # initialise starting index of sliding window
    start = 0

    # initialise maximum frequency
    maxf = 0

    # Create counter obejct to track frequency in sliding window
    count = collections.Counter()

    # iterate through string
    for i in range(len(s)):
        # print(s[i], " at index ", i)
        # print("maxf = ", maxf)
        # Increment counter
        count[s[i]] += 1
        # Update maximum frequency in the given window
        maxf = max(maxf, count[s[i]])
        # Increase size of window if it can get larger
        if i - start + 1 > maxf + k:
            # Reduce size of window
            count[s[start]] -= 1
            start += 1

    return len(s) - start


print(characterReplacement("AABABBA", 1))