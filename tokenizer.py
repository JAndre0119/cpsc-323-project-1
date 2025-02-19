from regex import identifer_regex, number_regex, comment_regex

# Define keywords, operators, and separators
KEYWORDS = {"int", "float", "if", "else", "return", "while", "for", "main"}
OPERATORS = {"+", "-", "*", "/", "=", "==", "!="}
SEPARATORS = {";", "(", ")", "{", "}", ","}

def assign_token(lexeme):
    # Classifies a lexeme and returns its corresponding token type

    if lexeme in KEYWORDS:
        return("KEYWORD", lexeme)
    elif lexeme in OPERATORS:
        return("OPERATOR", lexeme)
    elif lexeme in SEPARATORS:
        return("SEPARATOR", lexeme)
    elif number_regex(lexeme):
        return("NUMBER", lexeme)
    elif identifer_regex(lexeme):
        return("IDENTIFIER", lexeme)
    elif comment_regex(lexeme):
        return("COMMENT", lexeme)
    else:
        return("UNKNOWN", lexeme) # Catch any unrecognized lexeme
    
    # Example usage
    if __name__ == "__main__":
        test_lexemes = ["int", "x", "=", "42", ";", "// This is a comment"]
        for lexeme in test_lexemes:
            print(assign_token(lexeme))
