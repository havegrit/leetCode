class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if not magazine.count(char) >= ransomNote.count(char):
                return False
            ransomNote = ransomNote.replace(char, '')
        
        return True