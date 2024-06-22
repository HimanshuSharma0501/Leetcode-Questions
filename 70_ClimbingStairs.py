class Solution {
public:
    int arr[46];
    Solution(){
        arr[1]=1;
        arr[2]=2;
        arr[3]=3;
        for(int i=4;i<46;i++){
            arr[i]=arr[i-1]+arr[i-2];
        }
    }
    int climbStairs(int n) {
        return arr[n];
    }
};