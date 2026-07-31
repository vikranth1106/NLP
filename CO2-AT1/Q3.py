words = []
for i in range(3):
    word = input("Enter word: ")
    words.append(word)
print("\n{:<15}{:<12}{:<15}{:<18}{:<15}".format(
    "Word", "Stem", "Removed Affix", "Transformation", "Normalized"))
for word in words:
    stem = word
    affix = "-"
    ttype = "Unknown"
    if word.endswith("ing"):
        affix = "ing"
        stem = word[:-3]
        ttype = "Inflectional"
    elif word.endswith("ed"):
        affix = "ed"
        stem = word[:-2]
        ttype = "Inflectional"

    elif word.endswith("er"):
        affix = "er"
        stem = word[:-2]
        ttype = "Derivational"

    print("{:<15}{:<12}{:<15}{:<18}{:<15}".format(
        word, stem, affix, ttype, stem))