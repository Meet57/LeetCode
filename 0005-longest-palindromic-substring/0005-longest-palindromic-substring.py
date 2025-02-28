class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''Here what we basically do is we iterate through the string with one less character at the end and then we take two possibilities either a palindrome with one character in the centre being odd number length of palindrome and the other is even number for example "aba" and the other is "bb" then we give it to cheque palindrome with expansion function the indexes in the function will expand left and right till the time he gets the palindrome at maximum and after that we just compare it with the odd and even and the previous longest penidrome and then return the result'''

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