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
            
        reversedString = s[::-1]
        
        return True if reversedString == s else False