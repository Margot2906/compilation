
import re
import sys

regexExpressions = [
    # Whitespace
    (r'[ \n\t]+', None),

    # Example
    (r'\=', 'ASSIGN'),

    # TODO: Add the other regexes for your lexems
    # ...
]


class Lexem:
    '''
    Our token definition:
    lexem (tag and value) + position in the program raw text
    Parameters
    ----------
    tag: string
        Name of the lexem's type, e.g. IDENTIFIER
    value: string
        Value of the lexem,       e.g. integer1
    position: integer tuple
        Tuple to point out the lexem in the input file (line number, position)
    '''
    def __init__(self, tag=None, value=None, position=None):
        self.tag      = tag
        self.value    = value
        self.position = position

    def __repr__(self):
        return self.tag


class Lexer:
    '''
    Component in charge of the transformation of raw data to lexems.
    '''

    def __init__(self, lexems=None):
        self.lexems = lexems if lexems is not None else []

    def lex(self, inputText):
        '''
        Main lexer function:
        Creates a lexem for every detected regular expression
        The lexems are composed of:
            - tag
            - values
            - position
        SEE lexem for more info
        '''
        # Crawl through the input file
        for lineNumber, line in enumerate(inputText):
            lineNumber += 1
            position = 0
            # Crawl through the line
            while position < len(line):
                match = None
                for lexemRegex in regexExpressions:
                    pattern, tag = lexemRegex
                    regex = re.compile(pattern)
                    match = regex.match(line, position)
                    if match:
                        data = match.group(0)
                        # This condition is needed to avoid the creation of whitespace lexems
                        if tag:
                            lexem = Lexem(tag, data, [lineNumber, position])
                            self.lexems.append(lexem)
                        # Renew the position
                        position = match.end(0)
                        break
                # No match detected --> Wrong syntax in the input file
                if not match:
                    print("No match detected on line and position:")
                    print(line[position:])
                    sys.exit(1)

        return self.lexems