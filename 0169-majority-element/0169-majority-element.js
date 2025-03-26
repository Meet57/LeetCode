/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    var a = nums[0]
    var counter = 0

    for (num of nums){
        if(a === num){
            counter++
        }else{
            counter--
        }

        if(counter === 0){
            counter = 1
            a = num
        }
    }

    return a
};