import random

def randomize(file_name, num_choices):
    file = file_name
    items = []

    with open(file, "r", encoding="utf8") as fin:
        for line in fin:
            items.append(line.strip())

    #for item in items:
        #print(item)

    winner_list = []
    i = 1
    while i <= 3:
        index = random.randint(0, len(items)-1)
        winner = items[index]
        if winner not in winner_list:
            winner_list.append(winner.strip())
            print (f"{i}. {winner}")
            i += 1

    with open ("output.txt", "w", encoding="utf8") as fout:
        i = 1
        for name in winner_list:
            fout.write(f"{i}. ")
            fout.writelines([name])
            fout.write('\n')
            i += 1


if __name__ == '__main__':
    file_name = input("Enter name of file to select from: ")
    num_choices = int(input("How many users would you like to select? "))
    randomize(file_name, num_choices)