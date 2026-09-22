class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for i in strs:
            e+=str(len(i))
            e+="#"
            e+="".join(i)
        return e
            

    def decode(self, s: str) -> List[str]:
        array = []
        l = 0
        while l<len(s):
            r=l
            while s[r]!= '#':
                r+=1
            length = int(s[l:r])
            l = r+1
            
            r = l + length
            array.append(s[l:r])
            l = r
        return array
            



