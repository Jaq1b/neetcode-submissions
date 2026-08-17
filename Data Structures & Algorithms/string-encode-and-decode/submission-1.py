class Solution:
    def encode(self, strs: List[str]) -> str:
        e = ""
        for i in strs:
            e += "-" * len(i) + "!" + i   # "!" marks end of length-prefix, unambiguously
        return e

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            length = 0
            while s[j] == "-":     # count consecutive dashes = the length
                length += 1
                j += 1
            j += 1                  # skip the "!" terminator
            res.append(s[j:j+length])  # take exactly `length` characters
            i = j + length
        return res