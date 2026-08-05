words = []
for i in range(3):
    word = input("Enter word: ")
    words.append(word)
print("\n{:<15}{:<15}{:<15}{:<15}{:<15}".format(
    "Word", "Root", "Suffix", "Type", "Normalized"))
for word in words:
    root = word
    suffix = "-"
    mtype = "Unknown"
    
    if word.endswith("ing"):
        suffix = "ing"
        root = word[:-3]
        if root.endswith("ct"):
            root += "e"
        mtype = "Inflectional"

    elif word.endswith("ed"):
        suffix = "ed"
        root = word[:-2]
        if root.endswith("ct"):
            root += "e"
        mtype = "Inflectional"

    elif word.endswith("ion"):
        suffix = "ion"
        root = word[:-3]
        if root.endswith("connect"):
            root = "connect"
        mtype = "Derivational"

    print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(
        word, root, suffix, mtype, root))