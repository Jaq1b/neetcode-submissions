class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for i in strs:
            e += str(len(i))
            e+= "#"
            e+="".join(i)
        return e

    def decode(self, s: str) -> List[str]:

        i = 0
        output = []
        while i <len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            output.append(s[i:j])
            i=j
        return output
       