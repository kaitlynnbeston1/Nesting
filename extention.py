import random
""" Program of choice:
➊ favorite_languages = {
       'jen': ['python', 'ruby'],
       'sarah': ['c'],
       'edward': ['ruby', 'go'],
       'phil': ['python', 'haskell'],
       }
➋ for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
➌     for language in languages:
    print(f"\t{language.title()}")

    My plan is to add more people, randomise the list, use if statements to differentiate between singal and plural lists, and determine which languages have been used.
"""

favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c",],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
    }
favorite_languages["jake"] = ["python"]
favorite_languages["amy"] = ["c++",]
favorite_languages["Harlow"] = ["rust",]
favorite_languages["kaiser"] = ["python", "c#", "rust", "go"]
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"{name.title()}'s favorite language is:")
    else:
        print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(language) 
print("The following languages have been mentioned:")
langset = set()
for name, languages in favorite_languages.items():
    for language in languages:
        langset.add(language)
for lang in langset:
    print(lang)