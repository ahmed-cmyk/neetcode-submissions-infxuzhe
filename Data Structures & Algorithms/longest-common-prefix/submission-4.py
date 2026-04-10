class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        wLen = len(strs[0])
        match = ""

        for i in range(wLen):
            curr = ""
            for str in strs:
                if curr == "":
                    curr = str[i]
                if (i < len(str) and str[i] != curr) or (i + 1 > len(str)):
                    return match

            match += curr
    
        return match