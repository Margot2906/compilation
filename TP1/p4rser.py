# -*- encoding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


class ParsingException(Exception):
    pass


class Parser:
    def __init__(self, lexems):
        """
        Component in charge of syntaxic analysis.
        """
        self.lexems = lexems

    # ==========================
    #      Helper Functions
    # ==========================

    def accept(self):
        """
        Pops the lexem out of the lexems list.
        """
        self.show_next()
        return self.lexems.pop(0)

    def show_next(self, n=1):
        """
        Returns the next token in the list WITHOUT popping it.
        """
        try:
            return self.lexems[n - 1]
        except IndexError:
            self.error("No more lexems left.")

    def expect(self, tag):
        """
        Pops the next token from the lexems list and tests its type through the tag.
        """
        next_lexem = self.show_next()
        if next_lexem.tag != tag:
            raise ParsingException(
                f"ERROR at {str(self.show_next().position)}: Expected {tag}, got {next_lexem.tag} instead"
            )
        return self.accept()

    def remove_comments(self):
        """
        Removes the comments from the token list by testing their tags.
        """
        self.lexems = [lexem for lexem in self.lexems if lexem.tag != "COMMENT"]

    # ==========================
    #     Parsing Functions
    # ==========================

    def parse(self):
        """
        Main function: launches the parsing operation given a lexem list.
        """
        try:
            self.remove_comments()
            self.parse_program()
        except ParsingException as err:
            logger.exception(err)
            raise

    def parse_program(self):
        """
        Parses a program which is a succession of assignments.
        """
        self.expect("TYPE_INT")
        self.expect("KW_MAIN")
        self.expect("L_PAREN")
        self.expect("R_PAREN")
        self.expect("L_CURL_BRACKET")
        # Your code here!
        self.expect("R_CURL_BRACKET")

    def parse_assignment(self):
        """
        Parses an assignment.
        """
        self.expect("IDENTIFIER")
        self.expect("ASSIGN")
        self.expect("INTEGER")
        self.expect("TERMINATOR")


    def parse_declaration(self):
        """
        Parses a declaration.
        """
        self.expect("TYPE_INT")
        self.expect("IDENTIFIER")
        self.expect("TERMINATOR")


    def parse_expression(self):
        """
        Parses an expression.
        """
        self.expect("INTEGER")
        self.expect("ADDITION")
        self.expect("INTEGER")
        self.expect("TERMINATOR")


