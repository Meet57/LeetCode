class Solution:
    def isPalindrome(self, s: str) -> bool:

        # first and last index
        # check alnum
        # increment the index
        # check equal and increment

        i, j = 0, len(s) - 1
        n = len(s)

        while i <= j:
            while i < n and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1

            if i <= j:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1

        return True
