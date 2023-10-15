"""
Estimate: 15 Minutes
Actual:
"""

word_to_count = {}

text = input("Enter text: ")
words = text.split()
for word in words:
    number_of_words = word_to_count.get(word, 0)
    word_to_count[word] = number_of_words + 1
