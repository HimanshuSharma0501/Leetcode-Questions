class Solution
{
public:
    string countOfAtoms(string s)
    {
        stack<pair<string, int>> st;
        int i = 0;
        while (i < s.length())
        {
            if (s[i] == '(')
            {
                st.push({"(", 1});
                i += 1;
            }
            else if (s[i] == ')')
            {
                i += 1;
                int num = 0;
                while (i < s.length() && s[i] >= '0' && s[i] <= '9')
                {
                    num = num * 10 + (s[i] - '0');
                    i++;
                }
                int cnt = max(1, num);

                vector<pair<string, int>> v;
                while (st.top().first != "(")
                {
                    v.push_back({st.top().first, st.top().second * cnt});
                    st.pop();
                }
                st.pop();

                for (auto it : v)
                {
                    st.push({it.first, it.second});
                }
            }
            else
            {

                string temp = "";
                temp += s[i];
                int j = i + 1;

                while (j < s.length() && s[j] >= 'a' && s[j] <= 'z')
                {
                    temp += s[j];
                    j++;
                }

                int num = 0;

                while (j < s.length() && s[j] >= '0' && s[j] <= '9')
                {
                    num = num * 10 + (s[j] - '0');
                    j++;
                }
                int cnt = max(1, num);

                st.push({temp, cnt});
                i = j;
            }
        }

        map<string, int> mp;
        while (!st.empty())
        {
            mp[st.top().first] += st.top().second;
            st.pop();
        }

        string ans = "";
        for (auto it : mp)
        {
            ans += it.first;
            if (it.second > 1)
            {
                ans += to_string(it.second);
            }
        }

        return ans;
    }
};