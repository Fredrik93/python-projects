from typing import List

def Total (nums: List[int]) -> int:
    # loop over nums and find all subsets 
    for i in range(len(nums)):
    # save each subset and check its xor total 
        for j in range(len(nums)):
            print("subset: ", nums[i:j])
    # save total to an int totalNum
    # return totalNum

    return -1
