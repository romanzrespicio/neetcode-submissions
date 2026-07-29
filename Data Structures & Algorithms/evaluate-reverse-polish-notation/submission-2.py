class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == '+' or tokens[i] == '-' or tokens[i] == '*' or tokens[i] == '/':
                oper_two = stack.pop()
                oper_one = stack.pop()

                if tokens[i] == '+':
                    res = oper_one + oper_two
                elif tokens[i] == '-':
                    res = oper_one - oper_two
                elif tokens[i] == '*':
                    res = oper_one * oper_two
                elif tokens[i] == '/':
                    res = oper_one / oper_two
                
                stack.append(int(res))
                continue

            stack.append(int(tokens[i]))
        
        return stack[0]

                
