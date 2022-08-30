class Solution:
    def firstUniqChar(self, s: str) -> int:
        for c in s:
            if s.index(c) == s.rindex(c):
                return s.index(c)
        return -1