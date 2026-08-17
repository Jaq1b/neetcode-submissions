class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for i in strs:
            e += str(len(i)) + '#' + i
        return e
            

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":      # scan forward to find the delimiter
                j += 1
            length = int(s[i:j])    # everything before "#" is the length
            res.append(s[j+1:j+1+length])  # grab exactly `length` chars after "#"
            i = j + 1 + length      # jump past this string to start the next one
        return res