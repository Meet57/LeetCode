class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)

        # return False

        # So this one is the basic approach where you use the set and check whether the element is there in this set or not if the element is there in the set you return the true otherwise it loops through the whole array and returns false the another approach to the solution is like convert the whole list into set and if the set length is equal to the length of the list then yeah there is no duplicates but if the set length is less than the list then there is a duplicate

        seen = set(nums)

        return True if len(seen) < len(nums) else False