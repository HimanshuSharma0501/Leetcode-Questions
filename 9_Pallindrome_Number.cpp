class Solution
{
public:
    bool isPalindrome(int x)
    {
        int num = x;
        int ans = 0;
        if (x < 0)
        {
            return false;
        }
        else if (x == 0)
        {
            return true;
        }
        while (num != 0)
        {
            int digit = num % 10;
            ans = (ans * 10) + digit;
            num = num / 10;

            if (ans == x)
            {
                return true;
            }
            else if (ans > INT_MAX / 10 || ans < INT_MIN / 10)
            {

                return false;
            }
        }

        return false;
    }
};