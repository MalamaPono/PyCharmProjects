import random

# generate a valid pair and return it. Only fails when last person only has themselves to choose, in that
# case we just run it again. This is the best solution I can think of.
def generatePairs(names,doublePairs=True):
    pairings = {}
    notChosen = list(names)
    if doublePairs:
        for name in names:
            while True:
                chosen = random.choice(notChosen)
                if chosen == name and len(notChosen) == 1:
                    return False
                if chosen != name:
                    pairings[name] = chosen
                    notChosen.remove(chosen)
                    break
                else:
                    continue
    else:
        for name in names:
            while True:
                chosen = random.choice(notChosen)
                if chosen == name and len(notChosen) == 1:
                    return False
                if len(notChosen) == 1 and pairings[chosen] == name:
                    return False
                if chosen != name and pairings.get(chosen,0) != name:
                    pairings[name] = chosen
                    notChosen.remove(chosen)
                    break
                else:
                    continue
    return pairings


def printPairings(pairings):
    # sort pairings by key in alphabetical order
    pairings = sorted(pairings.items())

    for pairing in pairings:
        print('{} will gift {}'.format(pairing[0], pairing[1]))

def validateList(pairings,names):
    if sorted(pairings.keys()) == sorted(names) and sorted(pairings.values()) == sorted(names):
        return True
    else:
        return False

# get a valid list no matter how many names
names = input("Enter a list of names, seperating each name with a space: ")
names = names.split()
pairings = {}
while True:
    pairings = generatePairs(names, doublePairs=False)
    if pairings:
        break
    else:
        continue
printPairings(pairings)

# names = input("Enter a list of names, seperating each name with a space: ")
# names = names.split()
# names = ["Koa","Alana","Keli'i","Nohea","Five"]
# pairings = generatePairs(names,False)
# if pairings:
#     printPairings(pairings)


# check to see if double pairs = False never returns a double pair
# for i in range(200):
#     names = ["Koa","Alana","Keli'i","Nohea","Five"]
#     pairings = generatePairs(names,False)
#     if pairings:
#         for key,value in pairings.items():
#             if pairings[value] == key:
#                 print('fail')
#                 quit()
# print('success')

# check to see if double pairs = True actually does sometimes return double pairs
# pairs = 0
# for i in range(200):
#     names = ["Koa","Alana","Keli'i","Nohea","Five"]
#     pairings = generatePairs(names,True)
#     if pairings:
#         for key,value in pairings.items():
#             if pairings[value] == key:
#                 pairs+=1
# print(pairs/2)

# percent of times a valid list is returned for double pairs allowed
# count = 0
# for i in range(5000):
#     names = ["Koa", "Alana", "Keli'i", "Nohea", "Five"]
#     pairings = generatePairs(names,True)
#     if pairings:
#         count+=1
# print(round(count/5000,2) * 100)

# percent of times a valid list is returned for double pairs not allowed
# count = 0
# for i in range(5000):
#     names = ["Koa", "Alana", "Keli'i", "Nohea", "Five"]
#     pairings = generatePairs(names,False)
#     if pairings:
#         count+=1
# print(round(count/5000,2) * 100)