class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        
        l = 0 
        r = len(s) -1 
        answer = True
        

        while l<r:
            if s[l] == s[r] and s[l].isalnum() == True and s[r].isalnum() == True :
                l+=1
                r-=1
                answer = True
            elif s[l].isalnum() == False:
                l+=1
            elif s[r].isalnum() == False:
                r-=1
                
            else:
                answer = False
                break
        
        return answer
        