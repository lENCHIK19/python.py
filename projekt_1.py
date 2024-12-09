# Textový analyzátor
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jelena Půžová
email: elenabaskova19@gmail.com
"""
user_list = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

user_name = input("Enter your user name: ")
password = input("Enter your password: ")

if user_list.get(user_name) == password:
    print(f"Welcome to the app, {user_name}.\nWe have 3 texts to be anylized.")

else:
    print("Unregistered user, terminating the program.")
    exit()

TEXTS = {
    "1": """ Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
    "2": """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
    "3": """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""",
}

chosen_text = input("Enter a number between 1 and 3 to select: ")

if chosen_text.isdigit() and chosen_text in TEXTS:  # kontrola podminky
    my_text = TEXTS[chosen_text]

    split_text = my_text.split()  # rozdeleni texu na jednotliva slova
    word_count = len(split_text)  # pocet slov v vybranem textu

    titlecase_words = []  # slova zacinajici se velkymi pismeny
    for word in split_text:
        if word.istitle():
            titlecase_words.append(word)

    titlecase_words_count = len(
        titlecase_words
    )  # pocet slov zacinajicich velkymi pismeny

    uppercase_words = []  # slova psane velkymi pismeny
    for word in split_text:
        if word.isupper() and word.isalpha():
            uppercase_words.append(word)

    uppercase_words_count = len(uppercase_words)  # pocet slov psanych velkymi pismeny

    lowercase_words = []  # slova psane malymi pismeny
    for word in split_text:
        if word.islower():
            lowercase_words.append(word)

    lowercase_words_count = len(lowercase_words)  # pocet slov psanych malymi pismeny

    numeric_string = []  # obsah cisel v texu
    for word in split_text:
        if word.isdigit():
            numeric_string.append(int(word))

    numeric_string_count = len(numeric_string)  # pocet cisel
    sum_of_all_numbers = sum(numeric_string)  # suma vsech cisel

    print(f"There are {word_count} words in the selected text.")
    print(f"There are {titlecase_words_count} titlecase words.")
    print(f"There are {uppercase_words_count} uppercase words.")
    print(f"There are {lowercase_words_count} lowercase words.")
    print(f"There are {numeric_string_count} numeric strings.")
    print(f"The sum of all numbers is {sum_of_all_numbers}.")

else:
    print(f"The inserted number is incorrect, terminating the program.")

# Bohuzel jsem nevedela jak vytvorit tabulku na konci. 
# Kod jsem formatovala v Python Formatter.