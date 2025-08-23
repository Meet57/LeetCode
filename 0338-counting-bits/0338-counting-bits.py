class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2
        # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

        ans = [0] * (n + 1)
        for i in range(1, n+1):
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans