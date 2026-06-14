class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_r = {}
        count_m = {}

        for ch in ransomNote:
            if ch not in count_r:
                count_r[ch] = 1
            else:
                count_r[ch] += 1

        for ch in magazine:
            if ch not in count_m:
                count_m[ch] = 1
            else:
                count_m[ch] += 1

        for ch in count_r:
            if ch not in count_m:
                return False
            if (count_r[ch] > count_m[ch]):
                return False

        return True