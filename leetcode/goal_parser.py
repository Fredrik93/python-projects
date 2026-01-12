class GoalParser:
    def interpret(self, command: str) -> str:
        # split upp command, save to list 
        command = ["G","G"]
        
        # switch for each cmd 
        result = ""
        
        for cmd in command:
            match cmd:
                case "G":
                    result += "G"
                case "()":
                    result += "o"
                case "(al)":
                    result += "al"

        return result