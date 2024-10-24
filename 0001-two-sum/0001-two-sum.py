class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        # store the number as index, and value as key, in the complemets
        # if we get the pair for complement then we return them

        #example: {3:5}, target 10, we have 7 on index i, 
        #then tar - 7 = 3, and 3 is on index 5 so return 3 and i


        for i, number in enumerate(nums):
            n = target - number
            if n not in complements:
                complements[number] = i
            else:
                return [complements[n], i]