class Solution
{
public:
    bool canBeEqual(vector<int> &target, vector<int> &arr)
    {
        if (target.size() == arr.size())
        {
            vector<int> elementCounts(1001, 0);
            for (int i = 0; i < target.size(); i++)
            {
                elementCounts[target[i]]++;
                elementCounts[arr[i]]--;
            }
            for (int count : elementCounts)
            {
                if (count != 0)
                {
                    return false;
                }
            }
        }
        else
        {
            return false;
        }
    }
};