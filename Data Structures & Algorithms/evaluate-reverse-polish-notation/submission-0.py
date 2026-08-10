class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"*", "/","+","-"}
        
        for index in range(len(tokens)):
            listTerm = tokens[index]
            if listTerm not in operations: # if a number token
                stack.append(int(listTerm))
            else: # if an operation token
                term2 = int(stack.pop())
                term1 = int(stack.pop())
                
                match listTerm:
                    case "*":
                        stack.append(term1 * term2)
                    case "/":
                        stack.append(int(term1 / term2 ))
                    case "-":
                        stack.append(term1 - term2)
                    case "+":
                        stack.append(term1 + term2)

        return stack[0]


