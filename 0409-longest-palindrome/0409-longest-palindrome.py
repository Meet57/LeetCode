class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = {}
        count = 0
        
        for i in s:
            m[i] = m.get(i, 0) + 1

            if m[i] % 2 == 0:
                count += 2
        
        # so every character is set to be in front and end, now we can add anything to the middle as one character so if the length is greater then count then just add 1 to it as any character can fit in middle
        count += 1 if count < len(s) else 0

        return count