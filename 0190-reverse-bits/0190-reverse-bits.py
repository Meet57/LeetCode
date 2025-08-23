class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        num, idx =  0, 32 - len(s)

        for c in s:
            if c == "1":
                num += 2**idx
            idx += 1

        return num   