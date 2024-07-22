class Solution
{
public:
    vector<string> sortPeople(vector<string> &names, vector<int> &heights)
    {
        map<int, string> refMap;
        for (int i = 0; i < heights.size(); i++)
        {
            refMap[heights[i]] = names[i];
        }
        vector<string> res;
        auto a = refMap.end();
        a--;
        while (a != refMap.begin())
        {
            res.push_back(a->second);
            a--;
        }
        res.push_back(a->second);
        return res;
    }
};