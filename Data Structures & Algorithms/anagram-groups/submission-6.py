class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        e = defaultdict(list)
        for i in strs:
            sortedI = ''.join(sorted(i))
            e[sortedI].append(i)
        return list(e.values())

        