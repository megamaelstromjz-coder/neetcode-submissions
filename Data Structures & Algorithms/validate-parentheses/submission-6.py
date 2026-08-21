class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        bracs = {'{', '(', '['}

        if len(s) % 2 != 0:
            return False
        if s == "":
            return True
        if list(s)[0] not in bracs:
            return False
        

        for b in s:
            if b in bracs:
                stack.append(b)
            elif b == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
            elif b == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif b == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
        
        print(stack)
        if len(stack) == 0:
            return True
        else:
            return False
