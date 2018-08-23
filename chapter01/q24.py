'''
  Chapter 01   - https://www.nltk.org/book/ch01.html

  Section 08   - Exercises

  Question 24  -
    Write expressions for finding all words in text6 that meet the conditions
    listed below. The result should be in the form of a list of words:
    ['word1', 'word2', ...].
        a) Ending in ize
        b) Containing the letter z
        c) Containing the sequence of letters pt
        d) Having all lowercase letters except for an initial capital (i.e.,
        titlecase)

'''
from nltk.book import text6
import re
distinct_words = set(text6)

is_suffix_ize = lambda x: re.search('ize$', x, flags=re.IGNORECASE) != None
is_contain_z = lambda x: re.search('z', x, flags=re.IGNORECASE) != None
is_contain_pt = lambda x: re.search('pt', x, flags=re.IGNORECASE) != None
is_all_lower = lambda x: re.search('(^\w$|^\w[^A-Z]+)', x) != None

conditions = [is_suffix_ize, is_contain_z, is_contain_pt, is_all_lower]
letters = ['a', 'b', 'c', 'd']

ans = lambda c, l: list(filter(c, l))
for i in range(0, 4):
    print('Item %c:\n' % letters[i], ans(conditions[i], distinct_words))

