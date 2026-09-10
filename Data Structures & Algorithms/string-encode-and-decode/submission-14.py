class Solution:

    def encode(self, strs: List[str]) -> str:
        e  = ""
        for i in strs:
            e += str(len(i))
            e+= "#"
            e+=i
        return e

    def decode(self, s: str) -> List[str]:
       
        i = 0
        array = []

        while i<len(s):
            j = i
           
            
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i + length
            array.append(s[i:j])
            i=j
        return array
            
            