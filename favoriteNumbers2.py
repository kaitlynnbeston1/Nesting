# Dictionary of favorite numbers.
favNums = {
    "crystal": [4, 85, 100],
    "ozzy": [666, 1970],
    "debbie": [44, 59, 350],
    "kaitlynn": [77, 11, 666],
    "george": [0],
    }


# printing results of pole
for person, numbers in favNums.items():
    print(f"{person.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)
    print("\n")
