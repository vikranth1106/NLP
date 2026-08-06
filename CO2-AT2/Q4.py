words = ["activate", "activation", "reactivation"]

data = {
    "activate": {
        "prefix": "-",
        "root": "activate",
        "suffix": "-",
        "sequence": "Base Word"
    },
    "activation": {
        "prefix": "-",
        "root": "activate",
        "suffix": "ion",
        "sequence": "activate → activation"
    },
    "reactivation": {
        "prefix": "re",
        "root": "activate",
        "suffix": "ion",
        "sequence": "activate → activation → reactivation"
    }
}

print("Morphological Parsing Report\n")

for word in words:
    print("Original Word :", word)
    print("Prefix        :", data[word]["prefix"])
    print("Root          :", data[word]["root"])
    print("Suffix        :", data[word]["suffix"])
    print("Sequence      :", data[word]["sequence"])
    print("Normalized    :", data[word]["root"])
    print()