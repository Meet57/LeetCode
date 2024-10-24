class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"[": "]", "{": "}", "(": ")"}

        for i in s:
            if i in brackets:  # Directly check in the dictionary
                stack.append(i)
            else:
                if not stack or brackets[stack.pop()] != i:
                    return False
        
        return not stack  # Returns True if stack is empty, otherwise False
