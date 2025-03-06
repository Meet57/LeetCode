from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  # Output array
        l, r = 0, n - 1  # Two pointers at start and end

        # Fill the result array from the end
        for i in range(n - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):  # Compare absolute values
                result[i] = nums[l] ** 2
                l += 1  # Move left pointer
            else:
                result[i] = nums[r] ** 2
                r -= 1  # Move right pointer
        
        return result  # Return sorted squares