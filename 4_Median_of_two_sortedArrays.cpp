class Solution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        double median = 0;
        nums1.insert(nums1.end(), nums2.begin(), nums2.end());
        sort(nums1.begin(), nums1.end());
        if (nums1.size() % 2 == 0)
        {
            return median = (nums1[nums1.size() / 2.0] + nums1[(nums1.size() / 2.0) - 1]) / 2.0;
        }
        else
        {
            return median = nums1[nums1.size() / 2.0];
        }
    }
};