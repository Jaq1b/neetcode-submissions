class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        e = defaultdict(list)

        for i in strs:
            sortedS = ''.join(sorted(i))
            e[sortedS].append(i)

        
        return list(e.values())

            