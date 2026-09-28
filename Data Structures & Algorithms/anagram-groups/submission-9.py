class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            p[sortedS].append(s)
        
        return list(p.values())
        