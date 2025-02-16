class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ele in tokens:
            if ele not in '/*+-':
                stack.append(ele)
            else:
                right = int(stack.pop())
                left = int(stack.pop())

                if ele == "/":
                    stack.append(int(left/right))
                elif ele == "*":
                    stack.append(right * left)
                elif ele == "+":
                    stack.append(right + left)
                elif ele == "-":
                    stack.append(left - right)
            
        return int(stack.pop())