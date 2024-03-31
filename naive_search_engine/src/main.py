#!/usr/bin/env python

import sys
from subprocess import call

def main():
    if len(sys.argv) < 2:
        print(help_message())
        sys.exit(-1)
    
    if sys.argv[1] == "Indexer":
        if len(sys.argv) < 3:
            print(help_message())
            sys.exit(-1)
        
        call(["python", "term_frequency.py", "mapper"])
        call(["python", "term_frequency.py", "reducer"])
        call(["python", "inversed_document_frequency.py", "mapper"])
        # Call reducer for inversed_document_frequency
        call(["python", "indexer.py", "mapper"])
        # Call reducer for indexer
        call(["python", "doc_vectorizer.py", "reducer"])
    elif sys.argv[1] == "Query":
        if len(sys.argv) < 4:
            print(help_message())
            sys.exit(-1)
        
        # Call mapper for relevance_analyzer
        call(["python", "relevance_analyzer.py", "mapper"])
        # Call reducer for relevance_analyzer
    else:
        print(help_message())
        sys.exit(-1)

def help_message():
    return "Wrong arguments, help (arg1 arg2): \n ex1. Indexer /path/to input \n ex2. Query N 'query_string' "

if __name__ == "__main__":
    main()
