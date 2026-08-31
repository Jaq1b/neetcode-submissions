class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for i in strs:
            l = len(i)
            e+=str(l)
            e+=("#")
            e+=(i)
        return e

        
            


    def decode(self, s: str) -> List[str]:
        array = []
        p = 0
        while p<len(s):
            j = p
            while s[j] != '#':
                j+=1
            length = int(s[p:j])
            p = j +1
            j = p + length
            array.append(s[p:j])
            p = j
        return array
                
                
