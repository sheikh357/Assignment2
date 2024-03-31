#!/usr/bin/env python

import sys

def mapper():
    for line in sys.stdin:
        parts = line.strip().split('\t')
        doc_id, text = parts[0], parts[1]
        title = doc_id.split(' ')[1]  # Extracting title from doc_id
        doc_id = doc_id.split(' ')[0]  # Extracting doc_id from doc_id
        words = text.split()  # Tokenizing the text into words
        for word in words:
            # Emitting word, doc_id and count of 1
            print(f"{word.lower()},{doc_id}\t1")

if __name__ == "__main__":
    mapper()
