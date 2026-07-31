words = []
for i in range(3):
    word = input("Enter word: ")
    words.append(word)
print("\n{:<15}{:<30}{:<12}{:<12}{:<15}".format(
    "Word", "State Transition", "Type", "Root", "Normalized"))
for word in words:
    root = word
    state = "Start"
    ttype = "Unknown"
    if word.endswith("s"):
        root = word[:-1]
        state = "Start -> Root -> +s -> End"
        ttype = "Regular"
    elif word.endswith("ing"):
        root = word[:-3]
        if root.endswith("t"):
            root += "e"
        state = "Start -> Root -> +ing -> End"
        ttype = "Regular"

    elif word == "written":
        root = "write"
        state = "Start -> Irregular Verb -> End"
        ttype = "Irregular"

    print("{:<15}{:<30}{:<12}{:<12}{:<15}".format(
        word, state, ttype, root, root))