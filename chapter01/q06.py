'''
  Chapter 01   - https://www.nltk.org/book/ch01.html

  Section 08   - Exercises

  Question 06  - Produce a dispersion plot of the four main protagonists in
  Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby. What can
  you observe about the different roles played by the males and females in
  this novel? Can you identify the couples?
'''

from nltk.book import text2

four_main_protagonists = ["Elinor", "Marianne", "Edward", "Willoughby"]

text2.dispersion_plot(four_main_protagonists)

#count_occorrences = list(map(lambda x: (x, text2.count(x)), four_main_protagonists))
#print(count_occorrences)
print("Elinor and Marianne are most cited!")
print("Possible Couples:\n-> Elinor and Marianne\n-> Edward and Willoughby")
