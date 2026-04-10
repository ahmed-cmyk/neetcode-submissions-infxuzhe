class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for str in strs:
            sortedS = "".join(sorted(str))
            if sortedS in res:
                res[sortedS].append(str)
            else:
                res[sortedS] = [str]

        return list(res.values())