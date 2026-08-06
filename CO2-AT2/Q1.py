words = ["analyzing", "analysis", "analytical"]

for word in words:

    prefix = "-"
    suffix = "-"
    root = word
    transform = ""

    if word == "analyzing":
        root = "analyze"
        suffix = "ing"
        transform = "Inflectional"

    elif word == "analysis":
        root = "analyze"
        suffix = "sis"
        transform = "Derivational"

    elif word == "analytical":
        root = "analyze"
        suffix = "tic + al"
        transform = "Derivational"

    normalized = root

    print("Original Word :", word)
    print("Root          :", root)
    print("Prefix        :", prefix)
    print("Suffix        :", suffix)
    print("Type          :", transform)
    print("Normalized    :", normalized)
    print()