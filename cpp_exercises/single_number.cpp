#include <vector>

class Solution {
public:
    int singleNumber(std::vector<int>& nums) {
        int result = 0;
        for (int value : nums) {
            result ^= value;
        }
        return result;
    }
};
