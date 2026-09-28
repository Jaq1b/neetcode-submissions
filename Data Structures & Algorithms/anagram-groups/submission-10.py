class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p = defaultdict(list) #default dict of lists
        for s in strs: #loop through hte input of strings
            sortedS = ''.join(sorted(s)) #build a sorted version of s
            p[sortedS].append(s) #search through for common sortedS identifier and append s to where its grouped
        
        return list(p.values()) #return a list of p's values
        