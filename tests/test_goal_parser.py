from leetcode.goal_parser import GoalParser

def test_basic_case():
    gp = GoalParser()
    assert gp.interpret("G()(al)") == "Goal"


def test_basic_case2():
    gp = GoalParser()
    assert gp.interpret("G()()()()(al)") == "Gooooal"

def test_basic_case3():
    gp = GoalParser()
    assert gp.interpret("(al)G(al)()()G") == "alGalooG"