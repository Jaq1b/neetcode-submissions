class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for p in range(len(s)):
            if s[p].isalnum() == True:
                string += "".join(s[p])
            else:
                continue
        string = string.lower()
        count = 0
        for i in range(len(string)):
            if string[i] == string[::-1][i]:
                count +=1
            else:
                continue
            
                
        if count == len(string):
            return True
        else:
            return False
                
        