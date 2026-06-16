from collections import Counter


words = "the lazy fox fox".split()
c = Counter(words)
print(c.most_common(2))  # top 2

# wc = {}

# # umständlich
# for word in words:
#     if word in wc:
#         wc[word] += 1  # wc[word] = wc[word] + 1
#     else:
#         wc[word] = 1

# # bessere Weg
# wc = {}
# for word in words:
#     wc[word] = loot.get(word, 0) + inventory.get(word, 0)

# print(wc)
