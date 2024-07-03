class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = set("qwertyuiopQWERTYUIOP")
        secondRow = set("asdfghjklASDFGHJKL")
        thirdRow = set("zxcvbnmZXCVBNM")
        res = []
        for word in words:
            word_set = set(word)
            if word_set.issubset(firstRow) or word_set.issubset(secondRow) or word_set.issubset(thirdRow):
                res.append(word)
        return res