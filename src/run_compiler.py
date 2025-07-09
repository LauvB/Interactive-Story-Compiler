"""
Script to run the final compilation interactively.
You can choose to:
1. Compile story.txt
2. Run example_story_1
3. Run example_story_2
"""

from compiler import Compiler

def example_story_1(compiler_: Compiler):
    """Example: story with branching."""
    input_text = """
    scene: START
    text: "You are in a forest."
    choice: "Go left" -> WOLF
    choice: "Go right" -> GRANDMA_HOUSE

    scene: WOLF
    text: "The wolf appears!"
    choice: "Scream" -> HUNTER
    choice: "Run" -> START
    choice: "Surrender" -> END

    scene: HUNTER
    text: "The hunter accompanied you to your grandma's house."

    scene: GRANDMA_HOUSE
    text: "Your grandma is happy to see you."

    scene: END
    text: "The wolf ate you."
    """
    compiler_.compile(input_text)

def example_story_2(compiler_: Compiler):
    """Example: linear story"""
    input_text = """
    scene: START
    text: "You begin your journey alone in the forest."
    choice: "Continue" -> CLEARING

    scene: CLEARING
    text: "You reach a clearing. It's peaceful."
    choice: "Continue" -> END

    scene: END
    text: "You set up camp and rest for the night."
    """
    compiler_.compile(input_text)

if __name__ == "__main__":
    compiler = Compiler()

    print("---> Interactive Story Compiler <---")
    print("Choose an option:")
    print("1. Compile from story.txt")
    print("2. Run example_story_1")
    print("3. Run example_story_2")

    option = input("Enter 1, 2 or 3: ").strip()

    if option == "1":
        try:
            with open("src/story.txt", "r", encoding="utf-8") as f:
                code = f.read()
            compiler.compile(code)
        except FileNotFoundError:
            print("story.txt not found.")
    elif option == "2":
        example_story_1(compiler)
    elif option == "3":
        example_story_2(compiler)
    else:
        print("Invalid option. Exiting.")
