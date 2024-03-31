#!/usr/bin/env python

import sys

def query_to_vector(args):
    query = args[-1].lower()
    query_words = query.split()
    vector = {}
    for word in query_words:
        if word in vector:
            vector[word] += 1
        else:
            vector[word] = 1
    import json
    return json.dumps(vector)

if __name__ == "__main__":
    args = sys.argv[1:]
    result = query_to_vector(args)
    print(result)
