class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True

        # putting one block of list in front for base case taking as the first word will start with the first character
        for i in range(1, len(s)+1):
        # Looping from to len + 1 as it represents the dp list block where first element is NO Charcter but just a sharter pointer saying start of the word
            for j in range(i):
                # iterating every possible word from j to i index making it possibilities
                if dp[j] and s[j:i] in word_set:
                    # here d[j] means True, only when a word can be break from that point to further to create another word, the actual word should break in parts as it is important to make word from worddict, overlapping wont make any word
                    dp[i] = True
                    break
        
        return dp[len(s)]

        # I know MEET you know this just take time