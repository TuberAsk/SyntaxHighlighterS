import re

class SyntaxHighlighter:
    def __init__(self, code_text, language):
        self.code_text = code_text
        self.language = language

    def highlight_syntax(self, event=None):
        code = self.code_text.get("1.0", "end-1c")
        keywords = self.get_keywords_for_language(self.language)
        pattern = self.create_pattern(keywords)

        for tag in ["keyword", "string", "print", "()", "numbers", "[]", "<>", "{}"]:
            self.code_text.tag_remove(tag, "1.0", "end")

        for line_number, line in enumerate(code.split("\n"), start=1):
            for match in re.finditer(pattern, line):
                start_index = f"{line_number}.{match.start()}"
                end_index = f"{line_number}.{match.end()}"
                self.code_text.tag_add("keyword", start_index, end_index)
                self.code_text.tag_config("keyword", foreground="blue")
        for line_number, line in enumerate(code.split("\n"), start=1):
            for match in re.finditer(r'(["\'])(?:(?=(\\?))\2.)*?\1', line):
                start_index = f"{line_number}.{match.start()}"
                end_index = f"{line_number}.{match.end()}"
                self.code_text.tag_add("string", start_index, end_index)
                self.code_text.tag_config("string", foreground="orange")
        for line_number, line in enumerate(code.split("\n"), start=1):
            for match in re.finditer(r'\bprint\b', line):
                start_index = f"{line_number}.{match.start()}"
                end_index = f"{line_number}.{match.end()}"
                self.code_text.tag_add("print", start_index, end_index)
                self.code_text.tag_config("print", foreground="salmon")
        for line_number, line in enumerate(code.split("\n"), start=1):
            for match in re.finditer(r'\b\d+\b', line):
                start_index = f"{line_number}.{match.start()}"
                end_index = f"{line_number}.{match.end()}"
                self.code_text.tag_add("numbers", start_index, end_index)
                self.code_text.tag_config("numbers", foreground="purple")
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
    def get_keywords_for_language(self, language):
        keywords_dict = {
            "C": ["if", "include", "signed", "static", "else", "for", "while", "int", "return", "void", "struct", "goto", "do", "char", "double", "short", "long", "extern", "union", "float", "auto", "break", "enum", "register", "typedef", "switch", "sizeof", "volatile", "default", "unsigned", "const", "continue", "case"],
            "Python": ["if", "else", "for", "while", "def", "import", "return", "class", "elif", "as", "except", "try"],
            "Lua": ["if", "else", "for", "while", "function", "local", "return", "end", "then", "do", "break"],
            "JavaScript": ["if", "else", "for", "while", "function", "const", "return", "class", "break", "case", "catch", "continue", "debugger", "default", "delete", "do", "export", "extends", "false", "finally", "import", "in", "instanceof", "new", "null", "super", "switch", "this", "throw", "true", "try", "typeof", "var", "void", "with", "yield"],
            "HTML": ["DOCTYPE", "html", "head", "title", "body", "div", "p", "a", "img", "ul", "ol", "li", "h1", "h2", "h3", "h4", "h5", "h6", "meta", "link", "style", "script", "form", "input", "textarea", "button", "select", "option", "label", "table", "tr", "th", "td", "thead", "tbody", "tfoot", "col", "colgroup", "caption", "audio", "video", "source", "iframe", "nav", "header", "footer", "section", "article", "aside", "main", "figure", "figcaption", "details", "summary", "details", "summary", "fieldset", "legend", "canvas", "audio", "video", "map", "area", "abbr", "address", "blockquote", "cite", "code", "del", "dfn", "em", "i", "ins", "kbd", "mark", "q", "s", "samp", "small", "strong", "sub", "sup", "time", "u", "var", "wbr"],
            "SQL": ["SELECT", "FROM", "WHERE", "INSERT", "UPDATE", "DELETE", "CREATE", "ALTER", "DROP", "TABLE", "INTO", "VALUES"],
        }
        return keywords_dict.get(language, [])

    def create_pattern(self, keywords):
        return r'\b(?:' + '|'.join(keywords) + r')\b'

    # Ignore the fact that the code might be a little messy. If you want to contribute consider doing so. :D
