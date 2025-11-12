from typing import List
# wip 5 ^ 6 xor is missing in the list below so this loop is skipping that for some reason
def Total (nums: List[int]) -> int:
    totalXOR = 0
    list_of_sets = []
    for i in range(len(nums)):
        for j in range(len(nums)+1):
           tmp = nums[i:j]
           # Dont add empty sets to the list
           if tmp:
            list_of_sets.append(tmp)
    
    # iterate over each set and perform the xor operation
    for set in list_of_sets:
        print("set: " , set)
        if len(set) == 1:
           totalXOR = totalXOR + set[0]
        else:
            tmpXor = 0
            curr = 0
            for i in range(len(set)-1):
               if tmpXor != 0:
                  curr = set[i+1]
                  tmpXor = tmpXor ^ curr
               else:
                  tmpXor = set[i] ^ set[i+1]

            totalXOR = totalXOR + tmpXor


    return totalXOR

