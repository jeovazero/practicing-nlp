'''
  Chapter 01   - https://www.nltk.org/book/ch01.html

  Section 08   - Exercises

  Question 25  -
    Define sent to be the list of words ['she', 'sells', 'sea', 'shells', 'by',
    'the', 'sea', 'shore']. Now write code to perform the following tasks:

    a) Print all words beginning with sh
    b) Print all words longer than four characters

'''
import re
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']


print("Item a:")
begin_sh = list(filter(lambda x: re.search('^sh', x) != None, sent))
print(begin_sh)

print("\nItem b:")
longer_four_char = list(filter(lambda x: len(x) > 4, sent))
print(longer_four_char)
