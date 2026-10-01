class Solution:
    def isPalindrome(self, s: str) -> bool:
        l= 0
        r = len(s)
        s=s.lower()
        p = ""
        while l<len(s):
            if s[l].isalnum():
                p += "".join(s[l])
            l+=1
            
        print(p[::-1])
        return p == p[::-1]
        
            
        