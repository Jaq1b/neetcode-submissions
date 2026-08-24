class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        # Make a little counting book.
        # Every number gets a counter.
        for s in nums:
            res[s] += 1

        ans = []

        # We want to find the k numbers that show up the most.
        for i in range(k):

            # Look through our counting book.
            # Find the number (the KEY) with the biggest count (the VALUE).
            most_frequent = max(res, key=res.get)

            # Put that number into our answer box.
            ans.append(most_frequent)

            # We already picked this number,
            # so take it out before looking for the next one.
            del res[most_frequent]

        return ans