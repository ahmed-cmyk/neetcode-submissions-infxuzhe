class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = self.countLetters(s)
        tCount = self.countLetters(t)

        return sCount == tCount

    
    def countLetters(self, word: str) -> dict:
        res = {}

        for char in word:
            res[char] = res.get(char, 0) + 1

        return res
            