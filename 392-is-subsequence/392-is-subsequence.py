class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        
        curr_index = 0
        
        while True:
            works = False
            for c in t:
                if s[curr_index] == c:
                    curr_index += 1
                    
                if curr_index == len(s):
                    return True
            return False