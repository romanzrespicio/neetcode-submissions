class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok == "+":
                a, b = stack.pop(), stack.pop()
                res = a + b
                stack.append(res)
            elif tok == "-":
                a, b = stack.pop(), stack.pop()
                res = b - a
                stack.append(res)
            elif tok == "*":
                a, b = stack.pop(), stack.pop()
                res = a * b
                stack.append(res)
            elif tok == "/":
                a, b = stack.pop(), stack.pop()
                res = b / a
                stack.append(int(res))
            else:
                stack.append(int(tok))
        
        return stack[-1]
            