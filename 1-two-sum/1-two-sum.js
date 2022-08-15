/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let indices = {};
    for (let i = 0; i < nums.length; i++){
        let t = nums[i];
        let n = target - nums[i];
        if (indices[n] !== undefined){
            return [indices[n], i];
        }
        indices[t] = i;
    }
};