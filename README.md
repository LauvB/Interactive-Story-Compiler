# Interactive Story Compiler

## Description

Interactive Story Compiler is a compiler that transforms structured natural language stories into interactive HTML narratives. The project applies concepts from automata theory, context-free grammars (CFG), and formal language theory to produce educational, engaging, and visual outputs for exploring compilation principles.

Intended users include:

- Undergraduate computer science students
- Educators introducing compiler construction
- Hobbyist developers interested in storytelling and automation

## Features

- Transforms structured `.txt` files into interactive, browser-ready HTML stories.
- Demonstrates finite-state machine behavior with clickable choices.
- Lightweight, cross-platform, no installation required—works offline in any modern browser.
- GUI available (`story_gui.py`) for easier editing and compilation.

## User Stories

> _"As a student, I want to write simple branching stories in plain text so that I can visualize how compilers parse and generate structured outputs."_

> _"As a teacher, I want to demonstrate context-free grammars and lexical analysis using relatable examples, not abstract math."_

> _"As a developer, I want to generate interactive HTML stories from narrative input without needing advanced tools or servers."_

## Repository Structure

```
compiler_interactive_story/
│
├── src/                    # Source code for the compiler
│   ├── compiler.py         # Orchestrates the full pipeline
│   ├── lexer.py            # Lexical analyzer: tokenizes input
│   ├── syntactic.py        # Syntactic analyzer: parses token stream
│   ├── semantic.py         # Semantic analyzer: builds & validates internal structure
│   ├── story_gui.py        # Optional Tkinter interface (manual entry)
│   ├── run_compiler.py     # CLI runner that compiles story.txt
│   └── story.txt           # Example structured story input
│
├── tests/                  # Unit tests for each compiler phase
│   └── test.py
│
├── docs/                   # Report, slides, paper, poster, run cases
│   └── Report.pdf, Poster.pdf, etc.
│
├── README.md               # Full documentation and instructions
├── .gitignore              # Files/folders excluded from Git tracking
└── output.html             # Final generated HTML output (from compilation)
```

## How to Use

You can compile your interactive story in two ways: **from the command line** or **through a graphical interface**.

### Option A: Command-line (CLI)

1. Open a terminal and navigate to the project root.

2. Run the compiler:

```bash
python src/run_compiler.py
```

3. Select one of the options:

- Option 1: Compile the story written in `story.txt` (inside the `src/` folder).
- Options 2 and 3: Compile predefined examples.

This creates `output.html` in the project root.

4. Open `output.html` in any browser to explore your interactive story.

### Option B: Graphical Interface (GUI)

1. Launch the editor interface:

```bash
python src/story_gui.py
```

2. Write your story in the text box following this **structured format**:

```txt
scene: START
text: "You wake up in a dark cave."
choice: "Go left" -> DRAGON
choice: "Go right" -> EXIT

scene: DRAGON
text: "A dragon appears!"

scene: EXIT
text: "You found the way out."
```

**Important Rules**:

- The first scene must be named `START`.
- All keywords (`scene`, `text`, `choice`) must be lowercase.
- Text must be inside **double quotes** (`"`).
- Choices must follow the format: `choice "text" -> DESTINATION_ID`.
- Each scene must be defined only once.

3. Click **Compile** to validate and generate the interactive story.

4. The result (`output.html`) opens in your browser automatically.

### Explore Your Story

- The first scene (`START`) will appear by default.
- Click buttons to follow your own adventure.

## Module Overview

- **`lexer.py`** → Breaks down the input into meaningful tokens for processing.
- **`syntactic.py`** → Verifies the sequence of tokens follows the formal grammar.
- **`semantic.py`** → Checks references and builds the internal structure of the story.
- **`compiler.py`** → Generates the interactive HTML narrative from the validated story.
- **`story_gui.py`** → Graphical interface for editing and compiling stories.
- **`run_compiler.py`** → Command-line tool to run example stories.

## Requirements

- Python 3.x
- No external libraries required

## Run Cases

See detailed examples in [docs/run_cases.md](docs/run_cases.md)

## License

MIT License — use freely for learning and non-commercial projects.
