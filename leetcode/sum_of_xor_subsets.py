from typing import List

def Total (nums: List[int]) -> int:

    list_of_sets = []
    for i in range(len(nums)):
        for j in range(len(nums)+1):
           tmp = nums[i:j]
           # Dont add empty sets to the list
           if tmp:
            list_of_sets.append(tmp)
    # save total to an int totalNum
    # return totalNum

    return -1
