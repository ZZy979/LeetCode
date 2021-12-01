// 评论区解法
class Solution {
public:
    bool isMatch(string s, string p) {
        return isMatch(s.c_str(), p.c_str());
    }
    
    bool isMatch(const char* s, const char* p) {
        if(*p == 0)
            return *s == 0;
        bool first_match = *s && (*s == *p || *p == '.');
        if(*(p + 1) == '*')
            return isMatch(s, p + 2) || (first_match && isMatch(s + 1, p));
        else
            return first_match && isMatch(s + 1, p + 1);
    }
};
