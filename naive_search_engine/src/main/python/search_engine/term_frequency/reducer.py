#!/usr/bin/env python

import sys

def reducer():
    current_word = None
    current_count = 0
    current_doc_ids = []

    for line in sys.stdin:
        key, value = line.strip().split('\t')
        word, doc_id = key.split(',')
        count = int(value)

        # Check if we are still processing the same word
        if word == current_word:
            current_count += count
            current_doc_ids.append(doc_id)
        else:
            # If we are starting to process a new word, emit the previous word's count
            if current_word:
                # Emitting word and its total count along with associated doc_ids
                doc_ids_str = ','.join(current_doc_ids)
                print(f"{current_word}\t{doc_ids_str},{current_count}")
            current_word = word
            current_count = count
            current_doc_ids = [doc_id]

    # Emit the count for the last word
    if current_word:
        doc_ids_str = ','.join(current_doc_ids)
        print(f"{current_word}\t{doc_ids_str},{current_count}")

if __name__ == "__main__":
    reducer()
