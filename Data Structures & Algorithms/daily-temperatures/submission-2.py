class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stackIDX, stackTEMP = stack.pop()
                res[stackIDX] = idx - stackIDX

            stack.append((idx, temp))

        return res