# Interactive Story Compiler

## Description

Interactive Story Compiler is a compiler that transforms structured natural language stories into interactive HTML narratives. The project applies concepts from automata theory, context-free grammars (CFG), and formal language theory to produce educational, engaging, and visual outputs for exploring compilation principles.

## Features

- Transforms structured `.txt` files into interactive, browser-ready HTML stories.
- Demonstrates finite-state machine behavior with clickable choices.
- Lightweight, cross-platform, no installation required—works offline in any modern browser.
- GUI available (`story_gui.py`) for easier editing and compilation.

## How to Use

1. Write your story in `story.txt` following the structured format:

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
- **`story_gui.py`** → Graphical interface for editing and compiling stories.
- **`run_compiler.py`** → Command-line tool to run example stories.

## Requirements

- Python 3.x
- No external libraries required

---

## Run Cases

### Valid Case 1 – Minimal Story with Two Choices

```txt
scene: START
text: "You wake up in a cave."
choice: "Go left" -> LEFT
choice: "Go right" -> RIGHT

scene: LEFT
text: "You enter the forest."

scene: RIGHT
text: "You walk toward the village."
```

**Expected Result**: Opens in browser with two clickable choices.

---

### Valid Case 2 – Linear Story with One Scene Only

```txt
scene: START
text: "The story ends before it begins."
```

**Expected Result**: Renders a single scene with no choices.

---

### Valid Case 3 – Linear Story Using "Continue"

```txt
scene: START
text: "You wake up in a peaceful meadow."
choice: "Continue" -> PATH

scene: PATH
text: "You walk along a narrow path."
choice: "Continue" -> LAKE

scene: LAKE
text: "You reach a quiet lake under the stars."
```

**Expected Result**: A linear story with a single button at each scene. The user progresses through multiple scenes by repeatedly choosing “Continue”.

---

### Valid Case 4 – Looping Back

```txt
scene: START
text: "Do you want to play again?"
choice: "Yes" -> START
choice: "No" -> END

scene: END
text: "Goodbye!"
```

**Expected Result**: Story loops back to the START scene if user chooses "Yes".

---

### Invalid Case 1 – Missing START Scene

```txt
scene: INTRO
text: "This story does not have a starting point."
```

**Error**:

```
Missing START scene. Every story must begin with scene: START
```

---

### Invalid Case 2 – Lexical Error (Unexpected Character)

```txt
scene: START
text: ...
```

**Error**:

```
Unexpected character: .
```

---

### Invalid Case 3 – Missing Quotes in Text

```txt
scene: START
text: You wake up in a dark cave
```

**Error**:

```
Syntax error: expected STRING after TEXT, found Token(IDENTIFIER, You)
```

---

### Invalid Case 4 – Destination Scene Not Defined

```txt
scene: START
text: "Choose your path."
choice: "Go left" -> UNKNOWN
```

**Error**:

```
Undefined scene destinations: {'UNKNOWN'}
```

---

### Invalid Case 5 – Unreachable Scene

```txt
scene: START
text: "You wake up in a dark cave."

scene: DRAGON
text: "You meet a dragon."
```

**Error**:

```
Unreachable scenes detected: {'DRAGON'}
```

---

## License

MIT License — use freely for learning and non-commercial projects.
