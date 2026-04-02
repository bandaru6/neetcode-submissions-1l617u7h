class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> count;
        for (auto const& num: nums) {
            count[num] += 1;
        }

        std::vector<std::vector<int>> freq = std::vector<std::vector<int>>(nums.size() + 1);

        for (auto const& [key, value]: count) {
            freq[value].push_back(key);
        }

        std::vector<int> res;
        for (int i = nums.size(); i > -1; i--) {
            if (res.size() < k && !freq[i].empty()) {
                for (auto const& val: freq[i]) {
                    res.push_back(val);
                    if (res.size() == k) {
                        break;
                    }
                }
            }

        }
        return res;
    }
};
