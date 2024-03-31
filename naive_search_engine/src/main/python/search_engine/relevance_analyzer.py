#!/usr/bin/env python

import sys

def mapper():
    for line in sys.stdin:
        parts = line.strip().split('\t')
        doc_id, text = parts[0], parts[1]
        title = doc_id.split(' ')[1]  # Extracting title from doc_id
        doc_id = doc_id.split(' ')[0]  # Extracting doc_id from doc_id
        print(f"{doc_id}\t{text}")

if __name__ == "__main__":
    mapper()
