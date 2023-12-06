input = open("input.txt").read().replace(" ", "").replace("\n", ":").split(":")
print(sum((int(input[1]) - hold) * hold > int(input[3]) for hold in range(1, int(input[1]))))