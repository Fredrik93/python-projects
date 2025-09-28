from typing import List

class Twosum:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        currentNumber = -1
        result: List[int] = []
        #loop over nums 
        for i, element in enumerate(nums):
            currentNumber = element
            for j,el in enumerate(nums):
                if i != j:
                    if currentNumber + el == target:
                        print("target!", currentNumber , " " , el )
                        result.append(i)
                        result.append(j)
                        return result
        
        # grab current number and loop over nums again (nested)
        # if current + number == target then save both indices to an arr "result"

        return []