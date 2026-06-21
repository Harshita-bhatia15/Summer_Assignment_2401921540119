class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop()
                if((char == ')' and ch == '(') or (char == '}' and ch == '{') or (char == ']' and ch == '[')):
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False