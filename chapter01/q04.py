'''
  Chapter 01   - https://www.nltk.org/book/ch01.html
  Section 08   - Exercises
  Question 04  - How many words are there in text2? How many distinct words are there?
'''

from nltk.book import text2

f_words = lambda t: len(t)
f_distinct_words = lambda t: len(set(t))

print("All words: ", f_words(text2))
print("Distinct words: ", f_distinct_words(text2))
