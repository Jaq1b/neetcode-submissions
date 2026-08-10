class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #create a dictionary of lists
        for s in strs: #loop through default list
            res["".join(sorted(s))].append(s) #sorts characters of s and joins thme into a dictionary key and hten appends the unsorted list to s
        return list(res.values())