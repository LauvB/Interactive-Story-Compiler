"""
This module implements the complete compilation process for the Interactive Story Compiler. 
It orchestrates the pipeline: lexical analysis -> syntactic analysis -> semantic analysis -> 
code generation. 

Author: Laura Beltrán & Santiago Sánchez
"""

from lexer import LexicalAnalyzer
from syntactic import SyntacticAnalyzer
from semantic import SemanticAnalyzer


class Compiler:
    """This class represents the behavior of the Interactive Story Compiler."""

    def compile(self, code: str, output_file: str = "output.html"):
        # Phase 1: Lexical Analysis
        lexer = LexicalAnalyzer()
        tokens = lexer.lex(code)

        # Phase 2: Syntactic Analysis
        syntactic = SyntacticAnalyzer(tokens)
        syntactic.parse()

        # Phase 3: Semantic Analysis
        semantic = SemanticAnalyzer(tokens)
        story_structure = semantic.analyze()

        # Phase 4: Code Generation (HTML)
        self.generate_html(story_structure, output_file)
        print(f"Compilation completed! Output written to '{output_file}'")

    def generate_html(self, story, output_file):
        html = ["<!DOCTYPE html>", "<html>", "<head>",
                "<meta charset='UTF-8'>",
                "<title>Interactive Story</title>",
                "<style>",
                "body { font-family: Arial, sans-serif; margin: 40px; }",
                ".scene { display: none; }",
                ".active { display: block; }",
                "button { margin: 5px; padding: 8px 12px; border-radius: 4px; }",
                "</style>",
                "<script>",
                "function showScene(id) {",
                "  document.querySelectorAll('.scene').forEach(s => s.classList.remove('active'));",
                "  document.getElementById(id).classList.add('active');",
                "}",
                "</script>",
                "</head>", "<body>"]

        for scene_id, content in story.items():
            html.append(f"<div class='scene' id='{scene_id}'>")
            html.append(f"<h2>{scene_id}</h2>")
            html.append(f"<p>{content['text']}</p>")
            for choice in content['choices']:
                html.append(
                    f"<button onclick=\"showScene('{choice['destination']}')\">{choice['text']}</button>"
                )
            html.append("</div>")

        # Start the first scene active
        html.append("<script>showScene('START');</script>")

        html.extend(["</body>", "</html>"])

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(html))
