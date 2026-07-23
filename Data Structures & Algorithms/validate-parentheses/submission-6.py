class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dct = {'}': '{', ')': '(', ']': '['}

        for i in s:
            if (i == '{') | (i == '(') | (i == '['):
                stack.append(i)
            elif stack and (stack[-1] == dct[i]):
                stack.pop()
            else:
                return False
            
            print(stack)

        return True if not stack else False