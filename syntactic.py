"""
This module represents the behavior of a syntactic analyzer  (parser) that checks whether 
the sequence of tokens conforms to the formal grammar (CFG) defined for the interactive 
story language.

Author: Laura Beltrán & Santiago Sánchez
"""
# GRAMMAR DEFINITION:
# <STORY>       -> <SCENELIST>
# <SCENELIST>   -> <SCENE> <SCENELIST> | ε
# <SCENE>       -> "scene:" <ID> "text:" <TEXT> <CHOICELIST>
# <CHOICELIST>  -> <CHOICE> <CHOICELIST> | ε
# <CHOICE>      -> "choice:" <TEXT> "->" <ID>
# <TEXT>        -> <STRING>
# <ID>          -> <IDENTIFIER>


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
        if self.current_token.type == "SCENE":
            self.advance()
            if self.current_token.type == "IDENTIFIER":
                scene_name = self.current_token.value
                self.advance()
                if self.current_token.type == "TEXT":
                    self.advance()
                    if self.current_token.type == "STRING":
                        narrative = self.current_token.value
                        self.advance()
                        self.choice_list()
                    else:
                        self.error("STRING after TEXT")
                else:
                    self.error("TEXT after scene identifier")
            else:
                self.error("IDENTIFIER after SCENE")
        else:
            self.error("SCENE")

    def choice_list(self):
        """Parses zero or more choices."""
        while self.current_token and self.current_token.type == "CHOICE":
            self.choice()

    def choice(self):
        """Parses a single choice."""
        self.advance()
        if self.current_token and self.current_token.type == "STRING":
            choice_text = self.current_token.value
            self.advance()
            if self.current_token and self.current_token.type == "ARROW":
                self.advance()
                if self.current_token and self.current_token.type == "IDENTIFIER":
                    destination = self.current_token.value
                    self.advance()
                else:
                    self.error("IDENTIFIER after ARROW")
            else:
                self.error("ARROW after choice text")
        else:
            self.error("STRING after CHOICE")

    def error(self, expected):
        """Raises a syntax error with details."""
        raise SyntaxError(f"Syntax error: expected {expected}, found {self.current_token}")
