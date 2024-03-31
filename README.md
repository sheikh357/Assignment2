# Assignment2

#Pre-processing
the first pre-processing file just simply takes a small amount of data for testing. What we have done is that we have taken the data from the csv and removed the columns that weren't needed. After removing them we have converted them into singular rows as the data contained multiple rows having the same ID so we mergered all the rows with the similar ids to a single row. Then we use the regular text pre-processing techniques on the section text.

#Pre-processing 2
Here we have taken a much bigger amount of data of 1-GB and all the preprocessing is taking place like in the previous file but on addition is made here we are spliting the data to csv's that would be splitted amongst the Azure Vm's that are generated.

Search Engine Description:
The search engine consists of two main components: Indexer and Ranker.

Indexer:
The Indexer processes input files to compute vectors for each document based on the Vector Space Model. It consists of three parts:

Inversed Document Frequency Counter: Calculates IDF for each unique word using MapReduce.
Term's Frequency Counter: Calculates TF for each word in each document using MapReduce.
Document Vectorizer: Produces vectors for each document by combining IDF and TF values.
Ranker:
The Ranker analyzes queries and returns the top N relevant documents using the index produced by the Indexer. It consists of three parts:

Query Vectorizer: Splits the input query into words and computes TF for each word.
Relevance Analyzer: Computes the relevance function between the query and each document using MapReduce.
Content Extractor: Extracts content from the relevant documents.
Search Engine Usage:
To use the search engine, execute the following commands:

Indexer: python Main.py /path/to/input/files
Ranker: python Main.py N "query text"
Note: N defines the maximum number of documents that the query must return.

This search engine is designed to be efficient and scalable, leveraging Python and Azure VMs for computation and storage.




