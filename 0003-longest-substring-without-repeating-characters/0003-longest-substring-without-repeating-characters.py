class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Approach: Sliding Window
        # Use a set to store characters and ensure uniqueness.
        charSet = set()
        left = 0
        max_length = 0
        # Use two pointers (left and right) to track the current substring.
        for right in range(len(s)):
            # If a duplicate is found, move left until all characters are unique again.
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            # Expand right and add characters to the set.
            charSet.add(s[right])
            # Keep track of the maximum length encountered.
            max_length = max(max_length, right - left + 1)
        
        return max_length