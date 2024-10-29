class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2


        all = 0
        two = 1
        one = 2

        for i in range(2,n):
            all = one + two
            two = one
            one = all

        return all