"""
Estimate: 15 Minutes
Actual: 7 Minutes
"""

word_to_count = {}

text = input("Enter text: ")
words = text.split()
for word in words:
    number_of_words = word_to_count.get(word, 0)
    word_to_count[word] = number_of_words + 1

# Could not get sorted feature to work.

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
