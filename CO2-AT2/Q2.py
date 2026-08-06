words = ["disagree", "agreement", "agreeable"]

data = {
    "disagree": {
        "prefix": "dis",
        "root": "agree",
        "suffix": "-",
        "type": "Derivational",
        "meaning": "Not agree"
    },
    "agreement": {
        "prefix": "-",
        "root": "agree",
        "suffix": "ment",
        "type": "Derivational",
        "meaning": "State of agreeing"
    },
    "agreeable": {
        "prefix": "-",
        "root": "agree",
        "suffix": "able",
        "type": "Derivational",
        "meaning": "Pleasant or acceptable"
    }
}

print("Morphological Parsing Report\n")

for word in words:
    print("Original Word :", word)
    print("Prefix        :", data[word]["prefix"])
    print("Root          :", data[word]["root"])
    print("Suffix        :", data[word]["suffix"])
    print("Type          :", data[word]["type"])
    print("Meaning       :", data[word]["meaning"])
    print("Normalized    :", data[word]["root"])
    print()