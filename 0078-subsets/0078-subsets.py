class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        # Backtracking function to generate subsets.
        # At each step, we have two choices: include the current element or skip it.
        # The recursion explores both possibilities, ensuring all subsets are generated.
        def backtrack(index, path):
            result.append(path[:])  # Store a copy of the current subset
            
            for i in range(index, len(nums)):  
                path.append(nums[i])  # Include the current element
                backtrack(i + 1, path)  # Recur with the next index
                path.pop()  # Backtrack by removing the last element
        
        backtrack(0, [])
        return result
