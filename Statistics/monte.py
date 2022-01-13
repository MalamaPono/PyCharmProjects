from random import randint

N = 100000

def simulate(N):
    K = 0
    for _ in range(N):
        prize_door = randint(1, 3)
        chosen_door = randint(1, 3)
        monte = 0
        switched_door = 0
        if chosen_door == prize_door:
            monte = randint(1, 3)
            while monte == prize_door:
                monte = randint(1, 3)
            switched_door = 6 - monte - chosen_door
        else:
            monte = 6 - prize_door - chosen_door
            switched_door = 6 - monte - chosen_door
        if switched_door == prize_door:
            K += 1

    return float(K) / float(N)


print(simulate(N))
