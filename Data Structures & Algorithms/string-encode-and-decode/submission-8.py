class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):

            # Find the "#" that comes after the length
            j = i

            while s[j] != "#":
                j += 1

            # Everything before "#" is the length
            length = int(s[i:j])

            # Move past the "#"
            i = j + 1

            # Grab exactly "length" characters
            word = s[i:i + length]

            result.append(word)

            # Move to the beginning of the next encoded word
            i += length

        return result