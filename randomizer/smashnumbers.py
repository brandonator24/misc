import random

def randforrand():
    return random.randint(0,9)

def gennums(numnums):
    randoms = []
    i = 0
    while i < numnums:
        temp_random = random.randint(0,9)
        if temp_random not in randoms:
            randoms.append(temp_random)
            i+=1
    
    return randoms

if __name__ == "__main__":
    nums = int(input("How many random numbers would you like to generate? (enter 0 for random) "))
    if nums == 0:
        numnums = randforrand()
    else:
        numnums = nums
    randoms = gennums(numnums)
    print('\n***')
    print(randoms)
    print('***\n\n IF YOUR DAMAGE % ENDS WITH ONE OF THESE NUMBERS GET FUCKED')
