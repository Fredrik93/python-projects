from typing import List


class EmpTarget:
    def numberOfEmployeesWhoMetTarget(self, hours:List[int], target:int) -> str:
        amountOfPeopleHittingTarget = 0
        # loop over list.
        for hour in hours:
            if hour >= target:
                amountOfPeopleHittingTarget += 1
        # if el == target then increment counter
        # return counter
        return amountOfPeopleHittingTarget
    
