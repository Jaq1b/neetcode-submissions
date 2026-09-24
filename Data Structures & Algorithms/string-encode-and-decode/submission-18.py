class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for i in strs:
            e += str(len(i))
            e+= "#"
            e += "".join(i)
        return e

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i<len(s):
            j=i
            length = 0
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j+1
            j = length+i
            ans.append(s[i:j])
            i = j
        return ans



