class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # loop over nums 
        ans = []
        for i, num in enumerate(nums):
            ans.append(nums[nums[i]])
            #print(ans)
        return ans

