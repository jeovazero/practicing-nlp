from nltk.book import text2

f_words = lambda t: len(t)
f_distinct_words = lambda t: len(set(t))

print("All words: ", f_words(text2))
print("Distinct words: ", f_distinct_words(text2))
