class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for char in s:
            if 'a' <= char <= 'z':
                pass
            elif '0' <= char <= '9':
                pass
            else:
                s = s.replace(char, '')
            
        reversedString = ""
        
        for i in range(len(s)-1, -1, -1):
            reversedString += s[i]
            
        if s != reversedString:
            return False
        
        return True