from typing import List

def Total (nums: List[int]) -> int:
    s = set()
    list_of_sets = []
    # loop over nums and find all subsets 
    for i in range(len(nums)):
    # save each subset and check its xor total                 
        for j in range(len(nums)):
           tmp = nums[i:j]
           # Dont add empty sets to the list
           if tmp:
            list_of_sets.append(tmp)
    # save total to an int totalNum
    # return totalNum

    return -1
