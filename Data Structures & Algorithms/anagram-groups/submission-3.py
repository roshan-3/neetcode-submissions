class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strmap = defaultdict(list)

        for string in strs:
            strmap["".join(sorted(string))].append(string)
        
        return list(strmap.values())