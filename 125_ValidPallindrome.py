class Solution(object):
    def isPalindrome(self, s):
        s=[c.lower() for c in s if c.isalnum()]
        if s==s[::-1]:
            return True
        return False
    