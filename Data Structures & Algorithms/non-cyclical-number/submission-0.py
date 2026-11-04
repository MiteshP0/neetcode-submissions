class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)   # slow = 1 step, fast = 2 steps

        while slow != fast:                    # loop until pointers meet
            fast = self.sumOfSquares(fast)     # fast step 1
            fast = self.sumOfSquares(fast)     # fast step 2
            slow = self.sumOfSquares(slow)     # slow step 1
        return True if fast == 1 else False    # met at 1 means happy

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10                     # peel last digit
            digit = digit ** 2                 # square it
            output += digit                    # add to total
            n = n // 10                        # strip last digit
        return output