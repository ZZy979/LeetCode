// 评论区解法
class Solution {
public:
    vector<int> findClosedNumbers(int num) {
        int n = __builtin_popcount(num);
        int a, b;
        for (a = num + 1; a > 0; ++a)
            if (__builtin_popcount(a) == n)
                break;
        for (b = num - 1; b > 0; --b)
            if (__builtin_popcount(b) == n)
                break;
        return {a > 0 ? a : -1, b > 0 ? b : -1};
    }
};
