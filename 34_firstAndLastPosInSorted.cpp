class Solution
{
public:
#define DPSolver ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    vector<int> getIndcies(vector<int> &nums, int startingIdx, int trgt)
    {
        int b = startingIdx;
        int e = startingIdx;
        int sz = nums.size();
        while (b >= 0 && e <= sz - 1)
        {
            bool change = false;
            if (b - 1 >= 0 && nums[b - 1] == trgt)
            {
                b--;
                change = true;
            }
            if (e + 1 < sz && nums[e + 1] == trgt)
            {
                e++;
                change = true;
            }
            if (!change)
                return {b, e};
        }
        return {b, e};
    }

    vector<int> searchRange(vector<int> &nums, int trgt)
    {
        DPSolver;
        if (nums.size() == 1)
            if (trgt == nums[0])
                return {0, 0};
            else
                return {-1, -1};
        // apply binary search to find the position of the first element.
        int b = 0;
        int e = nums.size() - 1;
        int m = (e + b) / 2;
        while (b < e)
        {
            if (nums[m] == trgt)
                return getIndcies(nums, m, trgt);

            else if (nums[m] < trgt)
                b = m + 1;
            else
                e = m;
            m = (e + b) / 2;
        }
        if (m < nums.size() && m >= 0 && nums[m] == trgt)
            return getIndcies(nums, m, trgt);

        return {-1, -1};
    }
};