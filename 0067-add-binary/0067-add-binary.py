class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        carry = 0
        result = []

        while i>=0 or j>=0 or carry:
            bita = int(a[i]) if i>=0 else 0
            bitb = int(b[j]) if j>=0 else 0
            
            total = bita + bitb + carry

            if total == 0:
                result.append('0')
                carry = 0
            elif total == 1:
                result.append('1')
                carry = 0
            elif total == 2:
                result.append('0')
                carry = 1
            elif total == 3:
                result.append('1')
                carry = 1
            
            j-=1
            i-=1
            
        return ''.join(result[::-1])

