"""
This module represents the behavior of a lexical analyzer that transforms the input story text 
into a list of tokens. The lexer uses regular expressions to recognize keywords (scene:, text:, 
choice:), identifiers, arrows (->), and strings (narrative text enclosed in quotes). 

Author: Laura Beltrán & Santiago Sánchez
"""

class Token:
    """This class represents a token with type and value."""

    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


class LexicalAnalyzer:
    """This class represents the lexical analyzer behavior for interactive stories."""

    def __init__(self):
        self.token_specification = [
            ("SCENE", r"scene:"),
            ("TEXT", r"text:"),
            ("CHOICE", r"choice:"),
            ("ARROW", r"->"),
            ("IDENTIFIER", r"[A-Za-z0-9_]+"),
            ("STRING", r"\".*?\""),  # quoted string
            ("NEWLINE", r"\n"),
            ("SKIP", r"[ \t]+"),
            ("MISMATCH", r"."),  # Anything else
        ]

    def lex(self, code):
        import re
        tokens = []
        tok_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in self.token_specification)

        for mo in re.finditer(tok_regex, code):
            kind = mo.lastgroup
            value = mo.group().strip()

            if kind == "MISMATCH":
                raise RuntimeError(f"Unexpected character: {value}")
            if kind == "SKIP" or kind == "NEWLINE":
                continue
            tokens.append(Token(kind, value))

        return tokens
