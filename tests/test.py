import SyntaxHighlighterS
from SyntaxHighlighterS.main import SyntaxHighlighter
import tkinter as tk

root = tk.Tk()
root.title("A simple Tkinter Application.")

code_text = tk.Text(root, wrap=tk.NONE, tabs="0.4c")
code_text.pack()

highlighter = SyntaxHighlighter(code_text, language="Python")
code_text.bind("<KeyRelease>", highlighter.highlight_syntax)

root.mainloop()