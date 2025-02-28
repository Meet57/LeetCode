class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkPalindromeWithExpansion(left, right):
            while left>=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]

        if len(s) <= 1:
            return s
        
        result = ""
        for i in range(len(s)-1):
            # for odd list palindrome center with one character
            odd = checkPalindromeWithExpansion(i,i)
            # for even list palindrome center with one character
            even = checkPalindromeWithExpansion(i,i+1)

            result = max(result, odd, even, key = len)
        
        return result