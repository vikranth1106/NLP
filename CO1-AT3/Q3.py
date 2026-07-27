import re

text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
Python programming is powerful.
"""

while True:
    print("\n----- MENU -----")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == '1':
        print("Dates:", re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text))

    elif choice == '2':
        print("Phone Numbers:", re.findall(r'\b[6-9]\d{9}\b', text))

    elif choice == '3':
        print("Hashtags:", re.findall(r'#\w+', text))

    elif choice == '4':
        print("Mentions:", re.findall(r'@\w+', text))

    elif choice == '5':
        prefix = input("Enter Prefix: ")
        pattern = r'\b' + re.escape(prefix) + r'\w*'
        print("Matches:", re.findall(pattern, text, re.IGNORECASE))

    elif choice == '6':
        suffix = input("Enter Suffix: ")
        pattern = r'\b\w*' + re.escape(suffix) + r'\b'
        print("Matches:", re.findall(pattern, text, re.IGNORECASE))

    elif choice == '7':
        word = input("Enter Word: ")
        pattern = r'\b' + re.escape(word) + r'\b'
        print("Matches:", re.findall(pattern, text, re.IGNORECASE))

    elif choice == '8':
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")