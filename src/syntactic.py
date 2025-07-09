"""
This module represents the behavior of a syntactic analyzer  (parser) that checks whether 
the sequence of tokens conforms to the formal grammar (CFG) defined for the interactive 
story language.

Author: Laura Beltrán & Santiago Sánchez
"""
# GRAMMAR DEFINITION:
# <STORY>       -> <SCENELIST>
# <SCENELIST>   -> <SCENE> <SCENELIST> | ε
# <SCENE>       -> "scene" ":" IDENTIFIER "text" ":" STRING <CHOICELIST>
# <CHOICELIST>  -> <CHOICE> <CHOICELIST> | ε
# <CHOICE>      -> "choice" ":" STRING "->" IDENTIFIER

class SyntacticAnalyzer:
    """This class represents the behavior of a syntactic analyzer."""

    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.pos = -1
        self.advance()

    def advance(self):
        """Advances to the next token."""
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    def parse(self):
        """Starts parsing the entire story."""
        while self.current_token is not None:
            self.scene()

    def scene(self):
        """Parses a single scene."""
        if not self._match("KEYWORD", "scene"):
            self.error("KEYWORD 'scene'")
        if not self._match("SYMBOL", ":"):
            self.error("':' after 'scene'")

        if not self._match("IDENTIFIER"):
            self.error("scene identifier")

        if not self._match("KEYWORD", "text"):
            self.error("KEYWORD 'text'")
        if not self._match("SYMBOL", ":"):
            self.error("':' after 'text'")

        if not self._match("STRING"):
            self.error("scene narrative (quoted string)")

        self.choice_list()

    def choice_list(self):
        """Parses zero or more choices."""
        while self.current_token and self.current_token.type == "KEYWORD" and self.current_token.value == "choice":
            self.choice()

    def choice(self):
        """Parses a single choice."""
        if not self._match("KEYWORD", "choice"):
            self.error("KEYWORD 'choice'")
        if not self._match("SYMBOL", ":"):
            self.error("':' after 'choice'")

        if not self._match("STRING"):
            self.error("choice text (quoted string)")

        if not self._match("SYMBOL", "->"):
            self.error("'->' after choice text")

        if not self._match("IDENTIFIER"):
            self.error("destination scene identifier")

    def _match(self, expected_type, expected_value=None):
        """Checks if the current token matches the expected type (and optionally value), then advances."""
        if self.current_token is None:
            return False
        if self.current_token.type != expected_type:
            return False
        if expected_value is not None and self.current_token.value != expected_value:
            return False
        self.advance()
        return True

    def error(self, expected):
        """Raises a syntax error with details."""
        raise SyntaxError(f"Syntax error: expected {expected}, found {self.current_token}")