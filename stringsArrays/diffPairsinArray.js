var findPairs = function(nums, k) {
    var c = 0;
    var arr = 0
    while(c < nums.length - 1){
        for(let i =  1; i < nums.length; i++){
            if( nums[c] - nums[i] === k){
                arr++
            }
        }
        c++

    }
    return arr
   
};