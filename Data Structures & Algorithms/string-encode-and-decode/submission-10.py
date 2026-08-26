class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> List[str]:
        array = []
        i = 0
        n = len(s)

        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            p = int(s[i:j])

            start_of_string = j + 1          # skip the single '#'
            end_of_string = start_of_string + p
            array.append(s[start_of_string:end_of_string])

            i = end_of_string
        return array