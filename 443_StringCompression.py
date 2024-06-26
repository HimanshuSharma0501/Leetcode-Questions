class Solution(object):
    def compress(self, chars):
        if not chars:
            return 0
        myChar=chars[0]
        count=0
        length=len(chars)
        chars.append("")
        for i in range(length+1):
            char=chars.pop(0)
            if char==myChar:
                count+=1
            else:
                if count==1:
                    chars.append(myChar)
                elif count>1:
                    chars.append(myChar)
                    chars+=(list(str(count)))
                myChar=char
                count=1
        return len(chars)