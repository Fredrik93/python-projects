class GoalParser:
    def interpret(self, command: str) -> str:
        # split upp command, save to list 
        
        
        # switch for each cmd 
        result = ""
        match command:
            case "G":
                result += "G"
            case "()":
                result += "o"
            case "(al)":
                result += "al"
        # concqternqte the result and return 

        return result