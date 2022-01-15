#include <vector>
using namespace std;

// implement the brute force version - Loop through each element x and find if there is another value that equals to (target - x)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // initialize vector ans
        vector<int> ans;
        
        for (int i = 0; i < nums.size(); i++){
            for (int j = i+1 ; i < nums.size(); j++){
                if (nums[j] == target - nums[i]){
                    ans.push_back(i);
                    ans.push_back(j);
                }
            }
        }
    return ans;}
};