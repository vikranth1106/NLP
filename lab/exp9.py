text = input("Enter words: ")

words = text.split()

for word in words:
    if word.endswith("ing"):
        print(word, "-> VBG")
    elif word.endswith("ed"):
        print(word, "-> VBD")
    elif word.endswith("ly"):
        print(word, "-> RB")
    else:
        print(word, "-> NN")