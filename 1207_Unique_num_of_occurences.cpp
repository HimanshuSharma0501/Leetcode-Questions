class Solution
{
public:
    bool uniqueOccurrences(vector<int> &arr)
    {
        vector<int> val;
        int size = arr.size();
        sort(arr.begin(), arr.end());
        int i = 0;
        while (i < size)
        {
            int count = 1;
            for (int j = i + 1; j < size; j++)
            {
                if (arr[i] == arr[j])
                {
                    count++;
                }
                else
                {
                    break;
                }
            }
            val.push_back(count);
            i = i + count;
        }
        size = val.size();
        sort(val.begin(), val.end());
        for (int i = 0; i < size - 1; i++)
        {
            if (val[i] == val[i + 1])
            {
                return false;
            }
        }
        return true;
    }
};