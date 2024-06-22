class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies=max(candies)
        greatestCandies=[]
        for candy in candies:
            greatestCandies.append(candy+extraCandies>=maxCandies)
        return greatestCandies