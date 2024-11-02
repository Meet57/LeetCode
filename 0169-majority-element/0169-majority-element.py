class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[math.floor(len(nums)/2)]

        a = nums[0]
        counter = 0

        for i in nums:
            if i == a:
                counter+=1
            else:
                counter-=1
            
            if counter == 0:
                a = i
                counter = 1
        
        return a