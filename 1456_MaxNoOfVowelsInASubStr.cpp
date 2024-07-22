class Solution
{
public:
    bool isvowel(char &c)
    {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
    int maxVowels(string s, int k)
    {
        int count = 0;
        int ans = 0;
        int i = 0;
        int j = 0;
        while (j < s.length())
        {
            if (isvowel(s[j]))
            {
                count++;
            }
            if (j - i + 1 == k)
            {
                ans = max(count, ans);
                if (isvowel(s[i]))
                {
                    count--;
                }
                i++;
            }
            j++;
        }

        return ans;
    }
};