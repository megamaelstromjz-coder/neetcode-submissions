class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        stack.append('§')

        if len(s) % 2 != 0:
            return False

        for index in range(len(s)):
            match s[index]:
                case '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                case ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                case ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                case '{': 
                    stack.append('{')
                    
                case '[': 
                    stack.append('[')
                case '(':
                    stack.append('(')
                case _:
                    return False
        if stack == ['§']:
            return True
        else:
            return False