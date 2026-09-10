class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        e = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            e[sortedS].append(s)
        return list(e.values())
        
        