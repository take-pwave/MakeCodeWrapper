#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Strip comments and docstrings from a file.
以下のURLのファイルを使用させて頂きました
https://gist.github.com/BroHui/aca2b8e6e6bdf3cb4af4b246c9837fa3
"""

import sys, token, tokenize

def do_file(fname):
    """ Run on just one file.

    """
    source = open(fname)
    mod = open(fname + ",strip", "w")

    prev_toktype = token.INDENT
    first_line = None
    last_lineno = -1
    last_col = 0

    tokgen = tokenize.generate_tokens(source.readline)
    for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tokgen:
        if 0:   # Change to if 1 to see the tokens fly by.
            print("%10s %-14s %-20r %r" % (
                tokenize.tok_name.get(toktype, toktype),
                "%d.%d-%d.%d" % (slineno, scol, elineno, ecol),
                ttext, ltext
                ))
        if slineno > last_lineno:
            last_col = 0
        if scol > last_col:
            mod.write(" " * (scol - last_col))
        if toktype == token.STRING and prev_toktype == token.INDENT:
            # Docstring
            mod.write("#--")
        elif toktype == tokenize.COMMENT:
            # Comment
            mod.write("##\n")
        else:
            mod.write(ttext)
        prev_toktype = toktype
        last_col = ecol
        last_lineno = elineno

if __name__ == '__main__':
    do_file(sys.argv[1])
