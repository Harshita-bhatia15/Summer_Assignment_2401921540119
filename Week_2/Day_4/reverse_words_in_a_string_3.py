class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i = 0

        for j in range(n+1):
            if (j == n or s[j] == ' '):
                left = i
                right = j-1
                while(left<=right):
                    s[left],s[right] = s[right],s[left]
                    left = left+1
                    right = right-1
                i = j+1
        result = ''.join(s)
        return result