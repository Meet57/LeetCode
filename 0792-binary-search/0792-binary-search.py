class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # binary search ma sorted array avve and try to avoid the 
        # rest of the array is possible based on the value of mid

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        
        return -1
        