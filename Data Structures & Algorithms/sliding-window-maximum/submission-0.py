# brute force O(n)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # use dequeu for easy pop operations. deque keepes track indices with value decreasing front to back
        l = r = 0 # keep track left/right poinyrt in window

        while r < len(nums): #traverse until r passes the end

            while q and nums[q[-1]] < nums[r]: # basically saying: if index at back value is smaller than  new value we are checking then remove
                q.pop() # remove from back
            
            q.append(r)

            if l > q[0]: # if front index slid out window remove from front
                q.popleft()

            # check if seen atleast full window
            if (r+1) >= k:
                output.append(nums[q[0]]) # record front (current max) value
                l += 1 # advance left pointer

            r += 1 # advance right pointer

        return output
