import re

class SyntaxHighlighter:

    def __init__(self, code_text, language):
        self.code_text = code_text
        self.language = language

    def highlight_syntax(self, event=None):
        code = self.code_text.get("1.0", "end-1c")
        keywords = self.get_keywords_for_language(self.language)
        pattern = self.create_pattern(keywords)

        # Remove previous tags
        for tag in ["keyword", "string", "print", "()", "numbers", "[]", "<>", "{}"]:
            self.code_text.tag_remove(tag, "1.0", "end")

        # Find and tag all occurrences of keywords
        for line_number, line in enumerate(code.split("\n"), start=1):
            for match in re.finditer(pattern, line):
                start_index = f"{line_number}.{match.start()}"
                end_index = f"{line_number}.{match.end()}"
                self.code_text.tag_add("keyword", start_index, end_index)
                self.code_text.tag_config("keyword", foreground="blue")

        # Find and tag all occurrences of strings
        for line_number, line in enumerate(code.split("\n"), start=1):
            for match in re.finditer(r'(["\'])(?:(?=(\\?))\2.)*?\1', line):
                start_index = f"{line_number}.{match.start()}"
                end_index = f"{line_number}.{match.end()}"
                self.code_text.tag_add("string", start_index, end_index)
                self.code_text.tag_config("string", foreground="orange")

        # Find and tag all occurrences of 'print'
        for line_number, line in enumerate(code.split("\n"), start=1):
            for match in re.finditer(r'\bprint\b', line):
                start_index = f"{line_number}.{match.start()}"
                end_index = f"{line_number}.{match.end()}"
                self.code_text.tag_add("print", start_index, end_index)
                self.code_text.tag_config("print", foreground="salmon")

        # Find and tag all occurrences of numbers
        for line_number, line in enumerate(code.split("\n"), start=1):
            for match in re.finditer(r'\b\d+\b', line):
                start_index = f"{line_number}.{match.start()}"
                end_index = f"{line_number}.{match.end()}"
                self.code_text.tag_add("numbers", start_index, end_index)
                self.code_text.tag_config("numbers", foreground="purple")

#-------------------------------------------------------------------------------------
        # Find and tag all occurrences of '()' parentheses
        for line_number, line in enumerate(code.split("\n"), start=1):
            for match in re.finditer(r'[\{\}]', line):
                start_index = f"{line_number}.{match.start()}"
                end_index = f"{line_number}.{match.end()}"
                self.code_text.tag_add("{}", start_index, end_index)
                self.code_text.tag_config("{}", foreground="light blue")
                
        for line_number, line in enumerate(code.split("\n"), start=1):
            for match in re.finditer(r'[\[\]]', line):
                start_index = f"{line_number}.{match.start()}"
                end_index = f"{line_number}.{match.end()}"
                self.code_text.tag_add("[]", start_index, end_index)
                self.code_text.tag_config("[]", foreground="yellow")
        
        for line_number, line in enumerate(code.split("\n"), start=1):
            for match in re.finditer(r'[\<\>]', line):
                start_index = f"{line_number}.{match.start()}"
                end_index = f"{line_number}.{match.end()}"
                self.code_text.tag_add("<>", start_index, end_index)
                self.code_text.tag_config("<>", foreground="light blue")
                
        for line_number, line in enumerate(code.split("\n"), start=1):
            for match in re.finditer(r'[\(\)]', line):
                start_index = f"{line_number}.{match.start()}"
                end_index = f"{line_number}.{match.end()}"
                self.code_text.tag_add("()", start_index, end_index)
                self.code_text.tag_config("()", foreground="yellow")
#-------------------------------------------------------------------------------------

    def get_keywords_for_language(self, language):
        # Define keywords for each supported language
        keywords_dict = {
            "C": ["if", "include", "signed", "static", "else", "for", "while", "int", "return", "void", "struct", "goto", "do", "char", "double", "short", "long", "extern", "union", "float", "auto", "break", "enum", "register", "typedef", "switch", "sizeof", "volatile", "default", "unsigned", "const", "continue", "case"],
            "Python": ["if", "else", "for", "while", "def", "import", "return", "class", "elif"],
            "Lua": ["if", "else", "for", "while", "function", "local", "return", "end", "then", "do", "break"],
            "JavaScript": ["if", "else", "for", "while", "function", "const", "return", "class"],
            "HTML": ["DOCTYPE", "html", "head", "title", "body", "div", "p", "a", "img", "ul", "ol", "li", "h1"],
            "SQL": ["SELECT", "FROM", "WHERE", "INSERT", "UPDATE", "DELETE", "CREATE", "ALTER", "DROP", "TABLE", "INTO", "VALUES"],
        }
        return keywords_dict.get(language, [])

    def create_pattern(self, keywords):
        return r'\b(?:' + '|'.join(keywords) + r')\b'