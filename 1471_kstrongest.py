class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        length=len(arr)
        res=arr[(length-1)//2]
        i=0
        j=length-1
        result=[]
        while k>0:
            a=abs(arr[i]-res)
            b=abs(arr[j]-res)
            if a>b or (a==b and arr[i]>arr[j]):
                result.append(arr[i])
                i+=1
            else:
                result.append(arr[j])
                j-=1
            k-=1
        return result

        