"""
Script to run the final compilation

"""
from compiler import Compiler

compiler = Compiler()

with open("story.txt", "r", encoding="utf-8") as f:
    code = f.read()

compiler.compile(code)
