'''
  Chapter 01   - https://www.nltk.org/book/ch01.html

  Section 08   - Exercises

  Question 10  -
    Define a variable my_sent to be a list of words, using the syntax
    my_sent = ["My", "sent"] (but with your own words, or a favorite saying).

    a) Use ' '.join(my_sent) to convert this into a string.
    b) Use split() to split the string back into the list form you had to
    start with.

'''
# nao tem como (NTC)
my_sent = ["nice","to","meet","you"]
print("my_sent: ", my_sent)

my_sent_joined = ' '.join(my_sent)
print('Joined: ', my_sent_joined)

my_sent_joined_splitted = my_sent_joined.split(' ');
print('Splitted: ', my_sent_joined_splitted)

