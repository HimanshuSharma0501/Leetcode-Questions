class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i]!=9:
                digits[i]+=1
                return digits
            digits[i]=0
        #in case of all 9's
        return [1]+digits