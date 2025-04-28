class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start):
            if start == len(nums):
                # Creating a new nums by this statement
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res