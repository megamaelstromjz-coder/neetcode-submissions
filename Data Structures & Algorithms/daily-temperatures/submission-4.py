class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temps = enumerate(temperatures)
        
        stack = []
        next_greater_temp = {}

        for i,temp in temps:

            while stack and stack[-1][1] < temp:
                (a,b) = stack.pop()
                next_greater_temp[a] = i - a
            stack.append((i, temp))
        
        while stack:
            (a,b) = stack.pop()
            next_greater_temp[a] = 0

        return [v for k,v in sorted(next_greater_temp.items())]

