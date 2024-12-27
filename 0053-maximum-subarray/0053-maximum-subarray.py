
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        So in this question we use kadane's algo
        https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

        how it works
        max of sub array, it can the the number itself being the largest or the number before that with the sum of all previous numbers
        2 variables
        1. current -> checks which value is bigger, last sum or last sum + current index
        2. overall -> check which value is bigger, the last overall or CURRENT

        returns overall
        '''

        curr = nums[0]
        over = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i],nums[i]+curr)
            over = max(curr,over)

        return over