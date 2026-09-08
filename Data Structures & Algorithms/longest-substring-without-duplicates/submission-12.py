class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()   # tracks characters currently INSIDE the window [l, r]
        l = 0          # left edge of the window
        best = 0

        # r is the right edge — we grow the window one character at a time
        for r in range(len(s)):
            
            # If s[r] is already in our window, the window is no longer
            # valid (it has a repeat). We need to shrink from the LEFT
            # until the duplicate is gone — not just reset a counter.
            while s[r] in seen:
                seen.remove(s[l])  # kick out the leftmost character
                l += 1              # shrink the window by moving left edge forward

            # At this point, s[r] is guaranteed NOT in seen —
            # safe to add it and grow the window on the right side.
            seen.add(s[r])

            # Current window size is (r - l + 1). Compare against best seen so far.
            best = max(best, r - l + 1)

        return best