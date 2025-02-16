class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            # Compare the first two i and continues as those are same in the loop
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            # First from the i and last from the list
            left, right = i+1, n-1

            # ensure intersaction
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    # Skip if the next one is duplicate with previous left
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
                    # Skip if the next one is duplicate with previous right
                    while left < right and nums[right] == nums[right +1]:
                        right -= 1
                # if total is not 0 then only two cases
                elif total < 0:
                    # adding the smallest number we have as it is sorted array
                    left += 1
                else:
                    # substracting the largest number we have as it is sorted array
                    right -= 1
            
        return res
                
