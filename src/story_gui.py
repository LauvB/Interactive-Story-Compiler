"""
Graphical user interface

Author: Laura Beltrán & Santiago Sánchez
"""

import tkinter as tk
from tkinter import messagebox
from compiler import Compiler
import webbrowser

EXAMPLE_STORY = '''scene: START
text: "You wake up in a dark cave."
choice: "Go left" -> DRAGON
choice: "Go right" -> EXIT

scene: DRAGON
text: "A dragon appears!"
choice: "Fight" -> END
choice: "Run away" -> EXIT

scene: EXIT
text: "You found the way out."

scene: END
text: "The dragon devours you."'''

INSTRUCTIONS = """  How to write your interactive story:

        • Each scene must start with:
        scene: <scene_id>

        • Then add the scene text:
        text: "your narrative here"

        • Choices are optional, format:
        choice: "label" -> destination


    🔒 Rules:

        • All text must go inside double quotes ("...")
        • scene_id and destination must be simple identifiers
        • Each destination scene must be defined later

        
    ✅ Minimum example:

        scene: START
        text: "Intro"
        choice: "Go" -> END

        scene: END
        text: "The end."
"""

class StoryCompilerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Story Compiler")
        self.root.geometry("1100x600")
        self.root.configure(bg="white")

        # Layout
        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.left_frame = tk.Frame(self.main_frame, bg="white")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))

        self.right_frame = tk.Frame(self.main_frame, bg="white", width=300)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Left: Text editor
        self.text_label = tk.Label(self.left_frame, text="Your Story Code:",
                                   font=("Segoe UI", 12, "bold"), bg="white", anchor="w")
        self.text_label.pack(anchor="w")

        self.text_area = tk.Text(self.left_frame, wrap=tk.WORD, font=("Consolas", 12),
                                 bg="#f5f5f5", fg="#000000", insertbackground="black")
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.insert("1.0", EXAMPLE_STORY)

        self.compile_button = tk.Button(self.left_frame, text="Compile", command=self.compile,
                                        bg="#0078d7", fg="white", font=("Segoe UI", 11, "bold"), padx=20, pady=5)
        self.compile_button.pack(pady=10)

        # Right: Instructions
        self.instructions_label = tk.Label(self.right_frame, text="Instructions",
                                           font=("Segoe UI", 12, "bold"), bg="white", anchor="w")
        self.instructions_label.pack(anchor="w", pady=(0, 5))

        self.instructions_text = tk.Text(self.right_frame, wrap=tk.WORD, font=("Segoe UI", 10),
                                         bg="#f9f9f9", fg="#000000", height=40)
        self.instructions_text.pack(fill=tk.BOTH, expand=True)
        self.instructions_text.insert("1.0", INSTRUCTIONS)
        self.instructions_text.config(state=tk.DISABLED)

    def compile(self):
        code = self.text_area.get("1.0", tk.END).strip()

        if not code:
            messagebox.showwarning("Input Required", "Please write a story before compiling.")
            return

        try:
            with open("src/story.txt", "w", encoding="utf-8") as f:
                f.write(code)

            compiler = Compiler()
            compiler.compile(code)

            messagebox.showinfo("Success", "Compilation completed! Opening output.html...")
            webbrowser.open("output.html")

        except Exception as e:
            error_message = str(e)
            messagebox.showerror("Compilation Error", f"{error_message}")

# Run
if __name__ == "__main__":
    root = tk.Tk()
    app = StoryCompilerGUI(root)
    root.mainloop()
