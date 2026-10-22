# O(n) and O(1)
# First Unique Char in String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # keep track of what seen so far using map, and record frequency
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1 # first pass to keep occurances

        for i, char in enumerate(s):
            if freq[char] == 1:
                return i # return index where char occurance is 1
    
        return -1
        