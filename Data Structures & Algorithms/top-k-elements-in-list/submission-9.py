class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)

        # Count how many times each number appears
        for num in nums:
            seen[num] += 1

        # Sort numbers by their frequency
        sorted_numbers = sorted(
            seen,
            key=seen.get,
            reverse=True
        )

        # Return the k most frequent numbers
        return sorted_numbers[:k]