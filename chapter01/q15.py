'''
  Chapter 01   - https://www.nltk.org/book/ch01.html

  Section 08   - Exercises

  Question 15  -
    Find all words in the Chat Corpus (text5) starting with the letter b.
    Show them in alphabetical order.

'''
from nltk.book import text5

start_with = lambda txt, x: len(txt) > 0 and txt[0] == x
start_with_b = lambda txt: start_with(txt, 'b')

words_starts_b = list(filter(start_with_b, text5))

sorted_words_starts_b = sorted(words_starts_b)
print("Words starting with the letter b:\n", sorted_words_starts_b)
