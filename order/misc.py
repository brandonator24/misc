def isalpha():
    names = []
    with open("notalpha.txt", 'r') as aList:
        for line in aList:
            names.append(line.strip())

    for name in enumerate(names):
        if (name > name+1):
            print(f"{name} is out of order")

    print("List scan done!")


if __name__ == '__main__':
    isalpha()