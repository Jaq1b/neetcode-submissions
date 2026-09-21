class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)
        new = ""
        s = s.lower()
        while l<r:
            if s[l].isalnum():
                new+=s[l]
            l+=1
            
        return new == new[::-1]
       