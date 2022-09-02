class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = defaultdict(list)
        for s in strs:
            k = "".join(sorted(list(s)))
            grouping[k].append(s)
        res = []
        for v in grouping.values():
            res.append(v)
        return res