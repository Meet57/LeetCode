# nums = [12, 13, 14, 15, 16, 17, 18, 1, 2, 3, 4, 5, 6, 7, 8]
# target = 5

# The list is sorted in two different half
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            # Here the base story is that the area is sorted but in two different half if you get the middle one and check the left and right side you will get either of the side being sorted so this conditions are for the first loop itself and after that it will be the normal binary search as it will always go in the first if condition
            # In the condition to check which side is sorted is just because we can put a comparator where being the lowest value and the highest value has our middle target value so it is basically the first if statement in the outer if else statement
            
            # Left ride is sorted
            if nums[left] <= nums[mid]:
                # Maybe in the left side
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
