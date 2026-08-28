class Solution:
    def isPalindrome(self, s: str) -> bool:
        e = ""
        for i in range(len(s)):
            if s[i].isalnum():
                e+=(s[i])
        e = e.lower()
        
       
        i = 0
        j = len(e)-1
       
        while i<j:
            if e[i] == e[j]:
                i+=1
                j-=1
            else:
                return False
           
           
        return True
           
        