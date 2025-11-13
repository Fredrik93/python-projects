from typing import List
import itertools
def Total (nums: List[int]) -> int:
   totalXOR = 0
   subsets = []

   # find all subsets 
   for i in range(len(nums)+1):
      subsets.extend(itertools.combinations(nums, i))

   # bitwise XOR of all subsets 
   for s in subsets:
      tmp = 0
      for digits in s:
         tmp ^= digits
      totalXOR += tmp
   return totalXOR

