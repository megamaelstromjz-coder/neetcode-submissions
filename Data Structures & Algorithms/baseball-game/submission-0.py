class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for op in operations:
            if op == "+":
                n1 = stack[-1]
                n2 = stack[-2]
                stack.append(n1+n2)
                print(stack)
            
            elif op == "C":
                stack.pop()
                print(stack)
               

            elif op == "D":
                stack.append(stack[-1] * 2)

            else:
                stack.append(int(op))

        return sum(stack)


            