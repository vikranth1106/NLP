words = []
for i in range(3):
    word = input("Enter word: ")
    words.append(word)
print("\n{:<15}{:<12}{:<12}{:<12}{:<15}{:<15}".format(
    "Word", "Prefix", "Root", "Suffix", "Type", "Normalized"))
for word in words:
    prefix = "-"
    suffix = "-"
    root = word
    mtype = "Unknown"
    if word.startswith("un"):
        prefix = "un"
        root = word[2:]
        mtype = "Derivational"
    if root.endswith("ness"):
        suffix = "ness"
        root = root[:-4]
        if root.endswith("i"):
            root = root[:-1] + "y"
        mtype = "Derivational"

    elif root.endswith("ly"):
        suffix = "ly"
        root = root[:-2]
        if root.endswith("i"):
            root = root[:-1] + "y"
        mtype = "Derivational"

    print("{:<15}{:<12}{:<12}{:<12}{:<15}{:<15}".format(
        word, prefix, root, suffix, mtype, root))