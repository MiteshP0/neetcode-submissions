class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # store seen elements in map so retrieval is O(1)
        for i, n in enumerate(nums): # use enumerate as it can get index and value
            diff = target - n 
            if diff in map:
                return [map[diff], i] # returns the index where diff is
            map[n] = i # key, value store and value is suppose to be index as that is what we want to return
        