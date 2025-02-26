from dfa import token_keywords, token_names

def get_token(lexeme):
    """
    Determines the token type of a given lexeme.

    Parameters:
        lexeme (str): The lexeme to classify.

    Returns:
        str: The token name (keyword or identifier).
    """
    if lexeme in token_keywords:
        return f"KEYWORD({lexeme})"
    else:
        return "IDENTIFIER"
