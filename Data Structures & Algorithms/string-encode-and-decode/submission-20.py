class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr = ""
        for i in strs:
            newstr += str(len(i))
            newstr+= "#"
            newstr+= "".join(i)
        return newstr
    def decode(self, s: str) -> List[str]:

        i = 0
        answer = []

        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            
            i = j +1
            j = i+length
            
            answer.append(s[i:j])
            i=j
        return answer
