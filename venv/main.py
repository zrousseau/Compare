import random

dict = {"Jackson": 1400, "Aaron": 1400, "Michael": 1400, "Benjamin": 1400, "Zach": 1400}
list = ["Jackson", "Aaron", "Michael", "Benjamin", "Zach"]

while(True):
    # Randomly pulls a person from the list ensure that the same person isn't pulled
    while(True):
        item1 = list[random.randrange(len(list))]
        item2 = list[random.randrange(len(list))]

        if(item1 != item2):
            break

    # Battle to the Death
    print(item1, " (", dict.get(item1), ")", " vs ", item2, " (", dict.get(item2), ")", sep="")
    winner = int(input("Choose 1 or 2"))

    # Some simple math based on chess ELO or something
    r1 = dict.get(item1)
    r2 = dict.get(item2)

    p1 = r1 / (r1+r2)
    p2 = r2 / (r1+r2)

    k = 30

    # Updates the ratings
    if(winner == 1):
        r1 = int((r1 + k * (1 - p1)))
        r2 = int((r2 + k * (0 - p2)))
    else:
        r1 = int((r1 + k * (0 - p1)))
        r2 = int((r2 + k * (1 - p2)))

    dict.update({item1: r1})
    dict.update({item2: r2})

    # print(dict)

    keepPlaying = input("Continue?\n")

    if(keepPlaying == "n" or keepPlaying == "no" ):
        break


print(dict)





