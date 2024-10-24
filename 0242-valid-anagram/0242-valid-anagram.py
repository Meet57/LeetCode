class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # 2 solutions
        # sort then and return
        # make hash and then check and return

        # return "".join(sorted(s)) == "".join(sorted(t))

        hash = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hash[s[i]] = hash.get(s[i], 0) + 1
            hash[t[i]] = hash.get(t[i], 0) - 1

        for i in hash.values():
            if i != 0:
                return False
        
        return True