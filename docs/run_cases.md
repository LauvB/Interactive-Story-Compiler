# Run Cases

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
text: "Wanna play?"
choice: "Yes" -> AGAIN
choice: "No" -> END

scene: AGAIN
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
Syntax error: expected scene narrative (quoted string), found Token(IDENTIFIER, You)
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
