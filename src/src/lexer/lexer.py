class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []

    def tokenize(self):
        # Simple tokenizer example
        self.tokens = self.source_code.split()
        return self.tokens
