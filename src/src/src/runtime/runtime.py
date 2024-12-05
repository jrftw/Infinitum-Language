class Runtime:
    def __init__(self, ast):
        self.ast = ast

    def execute(self):
        print("Executing program...")
        print("Program Output:", self.ast["program"])
