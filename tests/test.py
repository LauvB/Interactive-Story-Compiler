'''
These tests check:
- Valid and invalid tokens (lexer)
- Valid and incomplete scenarios (parser)
- References and structures (semantic)

Run: python -m unittest tests/test.py
'''

import unittest
from src.lexer import LexicalAnalyzer
from src.syntactic import SyntacticAnalyzer
from src.semantic import SemanticAnalyzer


class TestInteractiveStoryCompiler(unittest.TestCase):

    def setUp(self):
        self.lexer = LexicalAnalyzer()

    def test_lexer_valid_tokens(self):
        code = '''
        scene: START
        text: "Welcome to the story."
        choice: "Go on" -> END

        scene: END
        text: "Goodbye."
        '''
        tokens = self.lexer.lex(code)
        types = [t.type for t in tokens]
        self.assertIn("SCENE", types)
        self.assertIn("TEXT", types)
        self.assertIn("CHOICE", types)
        self.assertIn("STRING", types)
        self.assertIn("ARROW", types)
        self.assertIn("IDENTIFIER", types)
        self.assertEqual(len(tokens), 12)

    def test_lexer_invalid_character(self):
        code = 'scene: START\ntext: @\n'
        with self.assertRaises(RuntimeError) as context:
            self.lexer.lex(code)
        self.assertIn("Unexpected character", str(context.exception))

    def test_syntactic_valid(self):
        code = '''
        scene: START
        text: "Hello there."
        choice: "Next" -> NEXT

        scene: NEXT
        text: "This is the end."
        '''
        tokens = self.lexer.lex(code)
        parser = SyntacticAnalyzer(tokens)
        parser.parse()

    def test_syntactic_missing_text(self):
        code = 'scene: START\n'
        tokens = self.lexer.lex(code)
        parser = SyntacticAnalyzer(tokens)
        with self.assertRaises(SyntaxError) as context:
            parser.parse()
        self.assertIn("TEXT after scene identifier", str(context.exception))

    def test_semantic_valid(self):
        code = '''
        scene: START
        text: "Scene one."
        choice: "Go" -> TWO

        scene: TWO
        text: "Scene two."
        '''
        tokens = self.lexer.lex(code)
        parser = SyntacticAnalyzer(tokens)
        parser.parse()
        semantic = SemanticAnalyzer(tokens)
        scenes = semantic.analyze()
        self.assertIn("START", scenes)
        self.assertIn("TWO", scenes)

    def test_semantic_unreachable_scene(self):
        code = '''
        scene: START
        text: "Entry point."

        scene: ORPHAN
        text: "This scene is not reachable."
        '''
        tokens = self.lexer.lex(code)
        parser = SyntacticAnalyzer(tokens)
        parser.parse()
        semantic = SemanticAnalyzer(tokens)
        with self.assertRaises(Exception) as context:
            semantic.analyze()
        self.assertIn("Unreachable scenes", str(context.exception))

    def test_semantic_undefined_reference(self):
        code = '''
        scene: START
        text: "Begin here."
        choice: "Go" -> MISSING
        '''
        tokens = self.lexer.lex(code)
        parser = SyntacticAnalyzer(tokens)
        parser.parse()
        semantic = SemanticAnalyzer(tokens)
        with self.assertRaises(Exception) as context:
            semantic.analyze()
        self.assertIn("Undefined scene destinations", str(context.exception))
