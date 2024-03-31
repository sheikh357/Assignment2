#!/usr/bin/env python

import sys

def read_n_relevant_ids(N):
    result = []
    for _ in range(N):
        line = input()  # Read line from standard input
        result.append(line.strip())
    return result

if __name__ == "__main__":
    N = int(sys.argv[1])  # Read the value of N from command-line arguments
    relevant_ids = read_n_relevant_ids(N)
    for doc_id in relevant_ids:
        print(doc_id)
