class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sorted_word = "".join(sorted(word)) #to make chars into strings 

            if sorted_word not in groups: #checking if nothings there
                groups[sorted_word] = []
                

            groups[sorted_word].append(word)

        return list(groups.values())