from lexer.lexer import Lexer

def test_lexer():
    lexer = Lexer("print 'Hello, World!'")
    tokens = lexer.tokenize()
    assert tokens == ["print", "'Hello,", "World!'"]
