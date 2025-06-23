# Interactive Story Compiler

## Description

Interactive Story Compiler is a compiler that transforms structured natural language stories into interactive HTML narratives. The project applies concepts from automata theory, context-free grammars (CFG), and formal language theory to produce educational, engaging, and visual outputs for exploring compilation principles.

## Features

- Transforms structured `.txt` files into interactive, browser-ready HTML stories.
- Demonstrates finite-state machine behavior with clickable choices.
- Lightweight, cross-platform, no installation required—works offline in any modern browser.

## Project Structure

```
compiler_interactive_story/
├── lexer.py          # Lexical analyzer (tokens generation)
├── sintactic.py      # Syntactic analyzer (grammar validation)
├── semantic.py       # Semantic analyzer (cross-reference checking)
├── compiler.py       # Main compiler (output HTML generation)
├── story.txt         # Input: your interactive story
├── output.html       # Output: generated HTML (optional in version control)
├── test.py           # Test lexer + parser
├── test_semantic.py  # Full test lexer + parser + semantic
├── run_compiler.py   # Script to generate final HTML
├── .gitignore        # Ignore files like output.html
└── README.md         # This file
```

## How to Use

1. Write your story in `story.txt` following the structured format:

```txt
scene: START
text: "You wake up in a dark cave."
choice: "Go left" -> DRAGON
choice: "Go right" -> EXIT
```

2. Run the compiler:

```bash
python run_compiler.py
```

3. Open `output.html` in any browser to explore your interactive story.

## Module Overview

- **`lexer.py`** → Breaks down the input into meaningful tokens for processing.
- **`syntactic.py`** → Verifies the sequence of tokens follows the formal grammar.
- **`semantic.py`** → Checks references and builds the internal structure of the story.
- **`compiler.py`** → Generates the interactive HTML narrative from the validated story.

## Requirements

- Python 3.x
- No external libraries required.
