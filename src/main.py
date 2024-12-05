from lexer.lexer import Lexer
from parser.parser import Parser
from optimizer.optimizer import Optimizer
from runtime.runtime import Runtime

def main():
    print("Welcome to Infinitum-Language!")
    source_code = input("Enter your Infinitum-Language code: ")
    
    # Step 1: Lexical Analysis
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()

    # Step 2: Parsing
    parser = Parser(tokens)
    ast = parser.parse()

    # Step 3: Optimization
    optimizer = Optimizer(ast)
    optimized_ast = optimizer.optimize()

    # Step 4: Runtime Execution
    runtime = Runtime(optimized_ast)
    runtime.execute()

if __name__ == "__main__":
    main()
