class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0

        while (i < len(chars)):
            group = 0

            while (group+i < len(chars) and chars[group+i] == chars[i]):
                group = group+1

            chars[j] = chars[i]
            j = j+1

            if (group != 1):
                for k in str(group):
                    chars[j] = k
                    j = j+1

            i = i+group

        return j