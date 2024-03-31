class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for char in t:
        #     if s.count(char) == 0:
        #         return False
        
        if len(s) != len(t):
            return False
        
        while len(s) > 0:
            if s.count(s[0]) != t.count(s[0]):
                return False
            t = t.replace(s[0], '')
            s = s.replace(s[0], '')
            
        return True