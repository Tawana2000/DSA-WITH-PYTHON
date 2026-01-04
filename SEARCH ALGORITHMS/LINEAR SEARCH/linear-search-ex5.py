# Find the index of the first word that contains the target substring
"""
Input:
words = ["cat", "dog", "elephant", "cow"]
target = "ph"

Output:
2
"""

def substring_index(words, target):
    for index, word in enumerate(words):
        if target in word:
            return index
    return None
print(substring_index(["cat", "dog", "elephant", "cow"], "ph"))
