class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '{' or x== '[' or x== '(':
                stack.append(x)
            else:
                if not stack:
                    return False
                pop = stack.pop()
                if pop == '{' and x != '}':
                    return False
                elif pop == '(' and x != ')':
                    return False
                elif pop == '[' and x != ']':
                   return False
        return not stack