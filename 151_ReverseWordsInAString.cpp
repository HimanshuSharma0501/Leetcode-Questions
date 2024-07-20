class Solution
{
public:
    string reverseWords(string s)
    {
        stack<string> st; // Initialize an empty stack
        s += " ";
        string str = "";
        for (int i = 0; i < s.size(); i++)
        {

            if (s[i] == ' ')
            {
                if (str != "")
                    st.push(str);
                str = "";
            }
            else
            {
                str += s[i]; // constructing an individual word
            }
        }
        if (str != "")
        {
            st.push(str); // push each word into stack
        }
        string ans = "";
        while (!st.empty())
        {
            ans += st.top() + " "; // pop words from the stack and append them to a ans string
            st.pop();
        }
        ans.pop_back();
        return ans; // Return the reversed string.
    }
};