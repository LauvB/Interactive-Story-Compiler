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
                """
                    body {
                    font-family: 'Segoe UI', sans-serif;
                    background-color: #f4f4f9;
                    color: #333;
                    margin: 0;
                    padding: 40px;
                    line-height: 1.6;
                    }

                    h2 {
                    font-size: 28px;
                    color: #0078d7;
                    text-align: center;
                    margin-bottom: 20px;
                    }

                    p {
                    font-size: 18px;
                    margin-top: 10px;
                    text-align: center;
                    }

                    .scene {
                    display: none;
                    padding: 30px;
                    border-radius: 8px;
                    background-color: white;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                    max-width: 700px;
                    margin: auto;
                    }

                    .active {
                    display: block;
                    }

                    .button-group {
                    display: flex;
                    justify-content: space-between;
                    flex-wrap: wrap;
                    margin-top: 30px;
                    }

                    button {
                    padding: 10px 24px;
                    border: none;
                    border-radius: 5px;
                    background-color: #0078d7;
                    color: white;
                    font-size: 16px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                    flex: 1 1 auto;
                    margin: 5px;
                    }

                    button:hover {
                    background-color: #005ea6;
                    }
                                """,
                                "</style>",
                                "<script>",
                                """
                    function showScene(id) {
                    document.querySelectorAll('.scene').forEach(s => s.classList.remove('active'));
                    const target = document.getElementById(id);
                    if (target) target.classList.add('active');
                    }
                """,
                "</script>",
                "</head>", "<body>"]

        for scene_id, content in story.items():
            html.append(f"<div class='scene' id='{scene_id}'>")
            html.append(f"<h2>{scene_id}</h2>")
            html.append(f"<p>{content['text']}</p>")
            if content['choices']:
                html.append("<div class='button-group'>")
                for choice in content['choices']:
                    html.append(
                        f"<button onclick=\"showScene('{choice['destination']}')\">{choice['text']}</button>"
                    )
                html.append("</div>")
            html.append("</div>")

        # Start the first scene active
        html.append("<script>showScene('START');</script>")

        html.extend(["</body>", "</html>"])

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(html))

