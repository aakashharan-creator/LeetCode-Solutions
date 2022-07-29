class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:       
        result = []
        
        for word in words:
            mapping = {}
            letters = set()
            
            if len(word) != len(pattern):
                continue
            
            for c, d in zip(word, pattern):
                if c in mapping:
                    if mapping[c] != d:
                        break
                else:
                    if d in letters:
                        break
                    mapping[c] = d
                    letters.add(d)
            else:
                result.append(word)   
        
        return result