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

        # All steps hal zero che and then when you think of nth step two ways possible one and two, if one step taken then it has 2 way and if 2 step taken then just 1 way, add them and then think of the step below it again 2 possibilities, started with 2 to n becase the 2nd step will be taken in the case as 2 and  1 step ways as in 2 ways

        for i in range(2,n):
            all = one + two
            two = one
            one = all

        return all