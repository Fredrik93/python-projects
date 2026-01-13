from typing import List

class GoalParser:
    def interpret(self, command: str) -> str:
        # split upp command, save to list 
        commands = self.extract_commands(command)
        
        # switch for each cmd 
        result = ""
        
        for cmd in commands:
            match cmd:
                case "G":
                    result += "G"
                case "()":
                    result += "o"
                case "(al)":
                    result += "al"

        return result

    def extract_commands(self, command) -> List[str]:
        previousSymbol = ""
        commands = []

        for s in command:
            print(s)

            if previousSymbol == '(' and s == ')':
                print("found a cmd: ()")
                commands.append("()")

            if s == 'G':
                commands.append('G')

            if previousSymbol == '(' and s == 'a':
                commands.append('(al)')
            previousSymbol = s

        return commands
          
                