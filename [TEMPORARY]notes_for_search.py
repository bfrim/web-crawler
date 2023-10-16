# Notes for Vector Space Model and Cosine Similarity

# We need to compute a score between a word "w" and a document "d":
# tf(w, d) = (# of occurences of w in d) / (total # of words in d)

# The inverse document frequency of a word "w" (idf(w)):
# idf(w) = log((total # of documents) / (1 + (# of documents w appears in)))

# Third measure combines the last two.
# The tf-idf weght for a word "w" in a document "d":
# tfidf(w, d) = log(1 + tf(w, d)) * idf(w)

# How are we going to use Vector Space Model? We view each document as a vector.

# User's query is also represented as a document (a much shorter one at that).

# COSINE SIMILARITY
# We can measure similarity by comparing angle between search query document and any other document.
# How to compute the angle? Compute the cosine of the angle:
# Cosine(0*) = 1, Cosine(90*) = 0
# We end up with a measure in the range [0, 1]
# "./computing_cosine_similarity.png" right-hand part is for computing.
# (program a vector as a list)

# RUNTIME COMPLEXITY
# Calculate term frequencies during the crawl as opposed to during every search, no computation wasting (not related to query)
# Calculate idf values once the crawl is complete.
# Only calculate Cosine similarity suring the search.
# Once Cosine is done, sort it from highest to lowest, and then return the top 10 search results on one page.