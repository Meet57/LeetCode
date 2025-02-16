class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # for nums = [1, 2, 3, 4]
        # Left Pass (Prefix Product) → Compute product of all elements before i.
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        # result after Left Pass: [1, 1, 2, 6]

        # Right Pass (Suffix Product) → Compute product of all elements after i.
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        # result after Right Pass: [24, 12, 8, 6]

        return result