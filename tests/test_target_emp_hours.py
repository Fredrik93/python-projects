from leetcode.target_emp_hours import EmpTarget

def test_basic_case():
    sol = EmpTarget()
    assert sol.numberOfEmployeesWhoMetTarget([1,2,3],2) == 4

