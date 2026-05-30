#include <cctype>
class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.length() - 1;

        while (l <= r) {
            if (!isalnum(s[l])) {
                l +=1;
                continue;
            }
            if (!isalnum(s[r])) {
                r -= 1;
                continue;
            }
            char c1 = tolower(s[l]);
            char c2 = tolower(s[r]);
            if (c1 != c2) {
                cout << s[l] << endl;
                return false;
            }
            l += 1;
            r -= 1;
        }
        return true;
    }
};
