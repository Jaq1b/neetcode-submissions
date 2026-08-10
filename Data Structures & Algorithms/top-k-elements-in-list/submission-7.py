class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # dictionary to store each number and how many times it appears
        for num in nums:
            count[num] = 1 + count.get(num, 0)  # increment count for this number (default to 0 if not seen yet)

        arr = []  # will hold [frequency, number] pairs so we can sort by frequency
        for num, cnt in count.items():
            arr.append([cnt, num])  # store as [count, num] — count first so sorting orders by frequency

        arr.sort()  # sorts by count ascending (since count is the first element of each pair), num breaks ties


        res = []  # will hold the final answer: the k most frequent numbers
        while len(res) < k:
            res.append(arr.pop()[1])  # pop the highest-count pair from the end (since sorted ascending),
                                       # take [1] to grab the number itself (not its count)

        return res  # the k most frequent numbers, found this way