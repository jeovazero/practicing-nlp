'''
  Chapter 01   - https://www.nltk.org/book/ch01.html

  Section 08   - Exercises

  Question 09  -
    a) Define a string and assign it to a variable, e.g., my_string = 'My String'
    (but put something more interesting in the string). Print the contents of
    this variable in two ways, first by simply typing the variable name and
    pressing enter, then by using the print statement.

    b) Try adding the string to itself using my_string + my_string, or
    multiplying it by a number, e.g., my_string * 3. Notice that the strings
    are joined together without any spaces. How could you fix this?


'''
# nao tem como (NTC)
nice = "nice to meet you"
print('Single: ', nice)

double_nice = nice + nice
print('Double: ', double_nice)

triple_nice = nice * 3
print('Triple: ', triple_nice)

triple_nice_with_spaces = ' '.join([nice]*3)
print('\nNow, using \'join\' in a list of strings.')
print('Triple, with spaces: ', triple_nice_with_spaces)
