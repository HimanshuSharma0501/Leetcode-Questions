class Solution
{
public:
    int countSeniors(vector<string> &details)
    {
        int seniors = 0;
        for (auto &x : details)
        {
            int age = stoi(x.substr(11, 2));
            seniors += age > 60;
        }
        return seniors;
    }
};