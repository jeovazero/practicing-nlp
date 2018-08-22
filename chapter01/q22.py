'''
  Chapter 01   - https://www.nltk.org/book/ch01.html

  Section 08   - Exercises

  Question 22  -
    Find all the four-letter words in the Chat Corpus (text5). With the help
    of a frequency distribution (FreqDist), show these words in decreasing
    order of frequency.

'''
from nltk.book import text5
from nltk.probability import FreqDist

is_4_letter = lambda x: len(x) == 4

distinct_words = set(text5)
words_4_letter = list(filter(is_4_letter, distinct_words))

fdist = FreqDist(text5)

#sorting by decreasing order of frequency
words_4_letter_sorted = sorted(
        words_4_letter,
        key=lambda x: fdist[x],
        reverse=True
        )

print(words_4_letter_sorted)
