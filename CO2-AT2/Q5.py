words = ["create", "creates", "creating"]

data = {
    "create": {
        "suffix": "-",
        "category": "Base Form",
        "root": "create"
    },
    "creates": {
        "suffix": "s",
        "category": "Third Person Singular",
        "root": "create"
    },
    "creating": {
        "suffix": "ing",
        "category": "Present Participle",
        "root": "create"
    }
}

print("Inflectional Normalization Report\n")

for word in words:
    print("Original Word :", word)
    print("Suffix        :", data[word]["suffix"])
    print("Category      :", data[word]["category"])
    print("Root          :", data[word]["root"])
    print("Normalized    :", data[word]["root"])
    print()