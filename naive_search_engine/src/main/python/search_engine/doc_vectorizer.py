#!/usr/bin/env python

import sys

def reducer():
    for line in sys.stdin:
        parts = line.strip().split('\t')
        doc_id, text = parts[0], parts[1]
        title = doc_id.split(' ')[1]  # Extracting title from doc_id
        doc_id = doc_id.split(' ')[0]  # Extracting doc_id from doc_id
        words = text.split()  # Tokenizing the text into words
        vector = {}
        for word in words:
            word, tf_idf = word.split(',')
            vector[word] = tf_idf
        # Creating JSON object
        import json
        json_vector = json.dumps(vector)
        print(f"{doc_id}\t{json_vector}")

if __name__ == "__main__":
    reducer()
