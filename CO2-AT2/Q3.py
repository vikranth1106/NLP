words = ["govern", "government", "governance"]

data = {
    "govern": {
        "root": "govern",
        "affix": "-",
        "level": "Base Word"
    },
    "government": {
        "root": "govern",
        "affix": "ment",
        "level": "Level 1"
    },
    "governance": {
        "root": "govern",
        "affix": "ance",
        "level": "Level 1"
    }
}

print("Normalization Report\n")

for word in words:
    print("Original Word      :", word)
    print("Root Word          :", data[word]["root"])
    print("Affix              :", data[word]["affix"])
    print("Derivational Level :", data[word]["level"])
    print("Normalized Form    :", data[word]["root"])
    print()