class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)

        for i in range(n):
            if (s[i] != "]"):
                stack.append(s[i])

            else:
                s1 = ""
                while stack[-1] != "[":
                    s1 = stack.pop() + s1
                stack.pop()
                k = ""
                while stack != [] and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*s1)
        
        result = "".join(stack)
        return result
