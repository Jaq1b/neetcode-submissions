class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for i in range(len(strs)):
            e+= str(len(strs[i]))
            e+= "#"
            e+= "".join(strs[i])
        return e

    def decode(self, s: str) -> List[str]:   # we want to get a section of hte string until we hit a # and then we save that section as an int and add that section to the answer array
        i = 0
        e = ""
        section = ""
        answer = []
        while i<len(s):
            if s[i] != "#":
                e+= (s[i])
                i+=1
            else:
                i+=1
                e = int(e)
                while (e)>0:
                    section += s[i]
                    i+=1
                    (e)-=1
                answer.append(section)
                e = ""
                section = ""
        return answer

       