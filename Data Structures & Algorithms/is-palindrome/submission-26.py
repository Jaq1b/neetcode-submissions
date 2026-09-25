class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        s= s.lower()
        for c in s:
            if c.isalnum():
                newstr+=c
        return newstr == newstr[::-1]
                
            
        