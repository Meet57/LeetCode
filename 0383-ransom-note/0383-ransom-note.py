class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False

        m = {}

        for i in magazine:
            m[i] = m.get(i, 0) + 1
        
        for i in ransomNote:
            m[i] = m.get(i, 0) - 1
            if m[i] < 0:
                return False
        
        return True
        
        

    