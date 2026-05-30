

class Solution {
public:
    bool isValid(string s) {
        std::stack<char> st;
        std::unordered_map<char, char> closed_to_open;
        closed_to_open['}'] = '{';
        closed_to_open[')'] = '(';
        closed_to_open[']'] = '[';

        for (int i = 0;  i < s.length(); i++) {
            if (closed_to_open.contains(s[i])) {
                if (st.empty()) {
                    return false;
                }
                //std::cout << "Hello, World!" << std::endl;
                char top = st.top();
                st.pop();
                if (top != closed_to_open[s[i]]) {
                    return false;
                }
            } else {
                st.push(s[i]);
            }
        }

        return st.empty();
    }
};
