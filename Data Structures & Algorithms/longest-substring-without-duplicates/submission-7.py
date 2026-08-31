class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        streak = 1
        e = {}
        best = 0
        start = 0

        if len(s) < 2:
            return len(s)

        for i, num in enumerate(s):

            if num in e and e[num] >= start:
                start = e[num] + 1
                streak = i - start + 1

            if streak > best:
                best = streak

            e[num] = i
            streak += 1

        return best