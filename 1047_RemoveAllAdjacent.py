class Solution(object):
    def removeDuplicates(self, s):
        if len(s)==1:
            return s
        stack=[]
        for a in s:
            if stack and stack[-1]==a:
                stack.pop()
                continue
            stack.append(a)
        return "".join(stack)